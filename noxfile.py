from contextlib import contextmanager
from functools import wraps
from pathlib import Path
from shutil import rmtree
from tempfile import TemporaryDirectory
from typing import Callable

from nox import Session, session


HERE = Path(__file__).parent

SessionFunc = Callable[[Session], None]


def build_test_repo(install: bool = True) -> Callable[[SessionFunc], SessionFunc]:

    def decorator(session_func: SessionFunc) -> SessionFunc:
        # build a test repo from test-config.yaml

        @wraps(session_func)
        def wrapper(session: Session) -> None:
            session.install("cookiecutter")

            session.run("cookiecutter", "--config-file", "test-config.yaml", "--no-input", ".")
            if install:
                session.install("./test-repo")

            try:
                return session_func(session)
            finally:
                rmtree(HERE / "test-repo")

        return wrapper

    return decorator


def install_latest_idom(session_func: SessionFunc) -> SessionFunc:
    # install the latest version of IDOM by pulling it from the main repo

    @wraps(session_func)
    def wrapper(session: Session) -> None:
        try:
            session.run("git", "clone", "https://github.com/idom-team/idom.git", external=True)
            session.install("./idom[testing,stable]")
            session_func(session)
        finally:
            idom_dir = HERE / "idom"
            if idom_dir.exists():
                rmtree(idom_dir)

    return wrapper


@session
def test(session: Session) -> None:
    session.notify("test_suite")
    session.notify("test_style")


@session
@build_test_repo()
@install_latest_idom
def test_suite(session: Session) -> None:
    session.install("pytest")
    session.run("pytest", "./test-repo/tests", "--headless", "--import-mode=importlib")


@session
@build_test_repo(install=False)
def test_style(session: Session) -> None:
    session.install("black", "flake8")
    session.run("black", "test-repo", "--check")
    session.run("flake8", "test-repo")

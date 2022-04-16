from contextlib import contextmanager
from functools import wraps
from pathlib import Path
from shutil import rmtree
from tempfile import TemporaryDirectory
from typing import Callable

from nox import Session, session


HERE = Path(__file__).parent
TEMPLATE_DIR = HERE / "{{cookiecutter.repository_name}}"

SessionFunc = Callable[[Session], None]


def build_test_repo(install: bool = True) -> Callable[[SessionFunc], SessionFunc]:
    """Build a test repo from test-config.yaml before a session"""

    def decorator(session_func: SessionFunc) -> SessionFunc:
        @wraps(session_func)
        def wrapper(session: Session) -> None:
            _build_test_repo(session, install)
            return session_func(session)

        return wrapper

    return decorator


def install_latest_idom(session_func: SessionFunc) -> SessionFunc:
    # install the latest version of IDOM by pulling it from the main repo

    @wraps(session_func)
    def wrapper(session: Session) -> None:
        try:
            session.run(
                "git", "clone", "https://github.com/idom-team/idom.git", external=True
            )
            session.install("./idom[testing,starlette]")
            session_func(session)
        finally:
            idom_dir = HERE / "idom"
            if idom_dir.exists():
                rmtree(idom_dir)

    return wrapper


@session
def test(session: Session) -> None:
    session.notify("test_suite", posargs=session.posargs)
    session.notify("test_style")


@session
@build_test_repo()
@install_latest_idom
def test_suite(session: Session) -> None:
    session.chdir("test-repo")
    session.run("playwright", "install", "chromium")
    session.run("pytest", "tests", "--import-mode=importlib", *session.posargs)


@session
@build_test_repo(install=False)
def test_style(session: Session) -> None:
    session.install("black", "flake8")
    session.run("black", "--check", "test-repo", *list(map(str, HERE.glob("*.py"))))
    session.run("flake8", "test-repo")


def _build_test_repo(session: Session, install: bool) -> None:
    # Need to remove node_modules so cookiecutter doesn't think since the cookiecutter
    # will try to format those files if present
    for path in TEMPLATE_DIR.rglob("node_modules"):
        if path.is_dir():
            rmtree(path)

    session.install("cookiecutter")

    if (HERE / "test-repo").exists():
        # Run first so that after each test run you can inspect the generated template
        # code to do some debugging. This also has the added benefit of being rebust
        # against KeyboardInterrupt exceptions triggered by the user.
        rmtree(HERE / "test-repo")

    session.run("cookiecutter", "--config-file", "test-config.yaml", "--no-input", ".")
    if install:
        session.chdir("test-repo")
        session.install(".")
        session.install("-r", "requirements.txt")
        session.chdir("..")

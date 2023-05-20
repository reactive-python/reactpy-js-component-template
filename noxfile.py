from pathlib import Path
from shutil import rmtree
from typing import Callable

from nox import Session, session


HERE = Path(__file__).parent
TEMPLATE_DIR = HERE / "{{cookiecutter.repository_name}}"

SessionFunc = Callable[[Session], None]


@session(tags=["test"])
def test_suite(session: Session) -> None:
    build_test_repo(session)
    install_latest_reactpy(session)
    session.chdir("test-repo")
    session.run("playwright", "install", "chromium")
    session.run("pytest", "tests", "--import-mode=importlib", *session.posargs)


@session(tags=["test"])
def test_style(session: Session) -> None:
    build_test_repo(session, install=False)
    session.install("black", "flake8")
    session.run("black", "--check", "test-repo", *list(map(str, HERE.glob("*.py"))))
    session.run("flake8", "test-repo")


def build_test_repo(session: Session, install: bool = True) -> None:
    """Build a test repo from test-config.yaml"""
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


def install_latest_reactpy(session: Session) -> SessionFunc:
    # install the latest version of ReactPy by pulling it from the main repo
    try:
        session.install(
            "reactpy[testing,starlette] @ git+https://github.com/reactive-python/reactpy"
        )
    finally:
        reactpy_dir = HERE / "reactpy"
        if reactpy_dir.exists():
            rmtree(reactpy_dir)

import pytest
from idom.testing import open_selenium_chrome_driver_and_display_context
from selenium.webdriver.support.ui import WebDriverWait


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--headless",
        dest="headless",
        action="store_true",
        help="Whether to run browser tests in headless mode.",
    )


@pytest.fixture
def driver_wait_until(driver) -> WebDriverWait:
    """A :class:`WebDriverWait` object for the current web driver"""

    def wait_until(function):
        WebDriverWait(driver, 3).until(lambda driver: function())

    return wait_until


@pytest.fixture(scope="module")
def driver(driver_and_display_context):
    return driver_and_display_context[0]


@pytest.fixture(scope="module")
def display(driver_and_display_context):
    with driver_and_display_context[1]() as display:
        yield display


@pytest.fixture(scope="module")
def driver_and_display_context(driver_is_headless):
    with open_selenium_chrome_driver_and_display_context(
        headless=driver_is_headless
    ) as dvr_and_disp_ctx:
        yield dvr_and_disp_ctx


@pytest.fixture(scope="session")
def driver_is_headless(pytestconfig):
    return bool(pytestconfig.option.headless)

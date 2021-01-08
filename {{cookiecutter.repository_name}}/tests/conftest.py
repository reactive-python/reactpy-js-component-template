import pytest
from idom.testing import create_mount_and_server, create_simple_selenium_web_driver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait


def pytest_addoption(parser) -> None:
    parser.addoption(
        "--headless",
        dest="headless",
        action="store_true",
        help="Whether to run browser tests in headless mode.",
    )


@pytest.fixture
def mount(mount_and_server):
    with mount_and_server.mount() as mount:
        yield mount


@pytest.fixture(scope="session")
def server(mount_and_server):
    server = mount_and_server
    yield server
    server.stop()


@pytest.fixture(scope="session")
def mount_and_server():
    return create_mount_and_server()


@pytest.fixture
def driver_wait_until(driver) -> WebDriverWait:
    """A :class:`WebDriverWait` object for the current web driver"""

    def wait_until(function):
        WebDriverWait(driver, 3).until(lambda driver: function())

    return wait_until


@pytest.fixture(scope="session")
def driver(driver_is_headless):
    options = ChromeOptions()
    options.headless = driver_is_headless
    driver = create_simple_selenium_web_driver(driver_options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def driver_is_headless(pytestconfig):
    return bool(pytestconfig.option.headless)

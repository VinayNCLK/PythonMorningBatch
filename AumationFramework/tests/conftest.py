
import pytest
from base.webdriverfactory import WebdriverFactory


@pytest.yield_fixture(scope="class")
def onetimesetup(request,browser):
    wdf = WebdriverFactory(browser)
    driver = wdf.getWebdriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
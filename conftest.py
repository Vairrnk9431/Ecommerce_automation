import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


# use pyttest in addoption to avoid error
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="Specify the browser : chrome or firefox or edge")



@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("no browser supported")
    yield driver
    driver.quit()



# hook for adding enviroment info in html reports
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] ='Ecommerce Project,nopcommerce'
    config.stash[metadata_key] ['Test Module Name'] ='Admin Login Tests'
    config.stash[metadata_key] ['Tester name'] ='Vaibhav'

# hook for adding/modifying/deleting enviroment info in html reports
pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

   
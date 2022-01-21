import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from scr.page_objects.example_google_home import GoogleHome
from scr.page_objects.example_web_result_page import WebResults
from scr.settings import *
import os
from datetime import datetime



# Allows for browser options
os.environ['WDM_LOG_LEVEL'] = '0'
opts = Options()
opts.headless = True  # Test browse window will not be visible while test run


# Gets Command Line arguments
def pytest_addoption(parser):
    parser.addoption("--Datetime", action="store", default=datetime.today().strftime('%d.%m.%y.%H_%M'), help="Required for saving of screenshots")


# Initialize page objects
def page_object_init(request, driver):
    request.cls.home_page = GoogleHome(driver)
    request.cls.results_page = WebResults(driver)


# Checks for latest ChromeDriver version
@pytest.fixture(scope='session')
def path_to_chrome():
    return ChromeDriverManager(path=TEST_PATH).install()


# Initializes chrome driver and opens testing window, runs at the beginning of each test
# Closes test window at end of test
@pytest.fixture()
def chrome_driver_init(request, path_to_chrome):
    today = request.config.getoption("--Datetime")
    driver = webdriver.Chrome(options=opts, executable_path=path_to_chrome)
    request.cls.driver = driver
    page_object_init(request, driver)
    driver.get(URL)
    driver.maximize_window()
    yield driver, today
    driver.quit()


# Hook that takes a screenshot of the web browser for failed tests and adds it to the HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        feature_request = item.funcargs['request']
        nodeid = str(item.nodeid).replace("::", "_").replace(".py", "").replace("/", "_")[10:]
        driver, today = feature_request.getfixturevalue('chrome_driver_init')
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver.save_screenshot(f"./reports/screenshots/{today}/{nodeid}.png")
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra

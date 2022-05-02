import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from scr.page_objects.example_google_home import GoogleHome
from scr.page_objects.example_web_result_page import WebResults
from scr.page_objects.example_img_result_page import ImgResults
from scr.settings import *
import os
from datetime import datetime

# Allows for browser options
os.environ['WDM_LOG_LEVEL'] = '0'
opts = Options()
opts.headless = True  # Test browse window will not be visible while test run


# Gets Command Line arguments
def pytest_addoption(parser) -> None:
    parser.addoption("--Datetime", action="store", default=datetime.today().strftime('%d.%m.%y.%H_%M'),
                     help="Required for saving of screenshots")


# Initialize page objects
def page_object_init(request, driver: WebDriver) -> None:
    request.cls.home_page = GoogleHome(driver)
    request.cls.web_results_page = WebResults(driver)
    request.cls.img_results_page = ImgResults(driver)


# Checks for latest ChromeDriver version
@pytest.fixture(scope='session')
def path_to_chrome() -> str:
    return ChromeDriverManager(path=TEST_PATH).install()


# Initializes chrome driver and opens testing window, runs at the beginning of each test
# Closes test window at end of test
@pytest.fixture()
def chrome_driver_init(request, path_to_chrome: str) -> WebDriver and str:
    today = request.config.getoption("--Datetime")  # Used to save screenshot to correct folder
    driver = webdriver.Chrome(options=opts, executable_path=path_to_chrome)
    request.cls.driver = driver
    page_object_init(request, driver)

    # Given: I am on the Google Search Page
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

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from settings import *

#Allows for browser options
opts = Options()
opts.headless = True #Test browse window will not be visible while test run

#Checks for latest ChromeDriver version
#Initalizes chrome driver and opens testing window, runs at the beginning of each test
#Closes test window at end of test
@pytest.fixture()
def chrome_driver_init(request):
    driver = webdriver.Chrome(options=opts, executable_path=ChromeDriverManager(path=TEST_PATH).install())
    request.cls.driver = driver
    driver.get(URL)
    driver.maximize_window()
    yield
    driver.quit()
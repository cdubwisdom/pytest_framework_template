"""
Used solely for the development of new test scripts.

When writing new scripts have the Test class inherit this TestBase. This allows the IDE to suggest the methods from the Page Object classes.

DO NOT use when actually running tests. Pytest will be unable to initiate the driver otherwise. All Test Classes should have no inheritance when running tests.
This class is used ONLY to make writing new test methods easier.
"""
from selenium.webdriver.chrome.webdriver import WebDriver
from scr.page_objects.example_img_result_page import ImgResults
from scr.page_objects.example_web_result_page import WebResults
from scr.page_objects.example_google_home import GoogleHome


class Writer:
    def __init__(self, driver: WebDriver):
        self.home_page = GoogleHome(driver)
        self.web_results_page = WebResults(driver)
        self.img_results_page = ImgResults(driver)

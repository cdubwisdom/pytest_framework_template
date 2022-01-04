from selenium.webdriver.common.by import By
from scr.fixtures.extensions import *

#Base page that has methods usable across all page objects
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def image_results(self):
        find_element_and_click(self.driver, Selectors.IMAGE_RESULT_TAB)

    def all_results(self):
        find_element_and_click(self.driver, Selectors.ALL_RESULT_TAB)

    def news_results(self):
        find_element_and_click(self.driver, Selectors.NEWS_RESULT_TAB)


class Selectors:
    IMAGE_RESULT_TAB = (By.XPATH, '//a[text()="Images"]')
    ALL_RESULT_TAB = (By.XPATH, '//a[text()="All"]')
    NEWS_RESULT_TAB = (By.XPATH, '//a[text()="News"]')
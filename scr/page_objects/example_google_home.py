import scr.fixtures.constants as Constants
from scr.fixtures.extensions import *
from selenium.webdriver.common.by import By

#example of a page object
class GoogleHome:
    def __init__(self, driver):
        self.driver = driver

    def web_search(self, search_query):
        find_element_and_send_keys(self.driver, Selectors.SEARCH_BAR, search_query)
        find_element_and_click(self.driver, Selectors.SEARCH_BUTTON)


class Selectors:
    SEARCH_BAR = (By.XPATH, '//input[@title="Search"]')
    SEARCH_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
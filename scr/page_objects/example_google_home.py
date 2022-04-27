import scr.fixtures.constants as Constants
from scr.fixtures.extensions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# example of a page object
class GoogleHome:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def web_search(self, search_query: str) -> None:
        find_element_and_send_keys(self.driver, Selectors.SEARCH_BAR, search_query)
        find_element_and_click(self.driver, Selectors.SEARCH_BUTTON)

    def img_search(self, search_query: str) -> None:
        find_element_and_click(self.driver, Selectors.IMG_SEARCH)
        find_element_and_send_keys(self.driver, Selectors.SEARCH_BAR, search_query)
        find_element_and_send_keys(self.driver, Selectors.SEARCH_BAR, Keys.RETURN, clear=False)


class Selectors:
    SEARCH_BAR = (By.XPATH, '//input[@title="Search"]')
    SEARCH_BUTTON = (By.XPATH, '//center/input[@name="btnK"]')
    IMG_SEARCH = (By.XPATH, '//a[text()="Images"]')

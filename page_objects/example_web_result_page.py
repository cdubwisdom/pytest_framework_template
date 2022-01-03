import fixtures.constants as Constants
from fixtures.extensions import *
from selenium.webdriver.common.by import By
from page_objects.example_base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class WebResults(BasePage):
    def is_expected_result_url_listed(self, search_result):
        return wait_for_element_to_exist(self.driver, Selectors.RESULT_URL(self, search_result))


class Selectors:
    def RESULT_URL(self, url):
        element = (By.XPATH, f'//a[@href="{url}"]')
        return element

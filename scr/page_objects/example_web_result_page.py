import scr.fixtures.constants as Constants
from scr.fixtures.extensions import *
from selenium.webdriver.common.by import By
from scr.page_objects.example_base_page import BasePage


class WebResults(BasePage):
    def is_expected_result_url_listed(self, search_result: str) -> bool:
        return wait_for_element_to_exist(self.driver, Selectors.RESULT_URL(search_result))


class Selectors:
    @staticmethod
    def RESULT_URL(url: str) -> tuple[str, str]:
        element = (By.XPATH, f'//a[@href="{url}"]')
        return element

import scr.fixtures.constants as Constants
from scr.fixtures.extensions import *
from selenium.webdriver.common.by import By
from scr.page_objects.example_base_page import BasePage


class ImgResults(BasePage):
    def is_expected_result_img_listed(self, search_result: str) -> bool:
        return wait_for_element_to_exist(self.driver, Selectors.RESULT_IMG(search_result))


class Selectors:
    @staticmethod
    def RESULT_IMG(title: str) -> tuple[str, str]:
        element = (By.XPATH, f'//img[contains(@alt, "{title}")]')
        return element

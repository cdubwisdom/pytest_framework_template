from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def element_exists(driver: WebDriver, by: tuple[str, str]) -> bool:
    return driver.find_elements(*by).count > 0


# waits for element to exist(or disappear) on web page
def wait_for_element_to_exist(driver: WebDriver, by: tuple[str, str], seconds: int = 10, negative: bool = False) -> bool:
    wait = WebDriverWait(driver, seconds)

    # waiting for element to exist
    if not negative:
        try:
            wait.until(EC.presence_of_element_located(by))
            return True
        except TimeoutException:
            return False
    # wait for element not to exist
    else:
        try:
            wait.until_not(EC.presence_of_element_located(by))
            return True
        except TimeoutException:
            return False


# waits for element to exist and returns WebElement
def find_element_with_wait(driver: WebDriver, by: tuple[str, str], retry: int = 2) -> WebElement:
    attempts = 0
    while attempts < retry:
        try:
            wait_for_element_to_exist(driver, by)
            return driver.find_element(*by)
        except NoSuchElementException:
            time.sleep(5)
            attempts += 1
    raise NoSuchElementException(f"The element with selector {by} was not located within 2 attempts.")


# sends keyboard actions or text to element
def find_element_and_send_keys(driver: WebDriver, by: tuple[str, str], keys: str, clear: bool = True, retry: int = 2) -> None:
    element = find_element_with_wait(driver, by, retry)

    if clear:
        element.clear()
    element.send_keys(keys)


# Clicks on element
def find_element_and_click(driver: WebDriver, by: tuple[str, str], retry: int = 2) -> None:
    element = find_element_with_wait(driver, by, retry)
    element.click()


# Looks for a web alert and accepts it, if no alert found moves on
def accept_alert_if_visible(driver: WebDriver) -> None:
    try:
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        print("No Alert Displayed")


# Selects a dropdown option by its html text from element
def open_and_select_dropdown_by_text(driver: WebDriver, by: tuple[str, str], option: str, retry: int = 2) -> None:
    element = Select(find_element_with_wait(driver, by, retry))
    element.select_by_visible_text(option)


# Selects a dropdown option based on html value
def open_and_select_dropdown_by_value(driver: WebDriver, by: tuple[str, str], option: int, retry: int = 2) -> None:
    element = Select(find_element_with_wait(driver, by, retry))
    element.select_by_value(option)


# Verifies if text in element matches given string
def does_text_match(driver: WebDriver, by: tuple[str, str], text: str, retry: int = 2) -> bool:
    element = find_element_with_wait(driver, by, retry)
    try:
        assert element.text.find(text) != -1
        return True
    except AssertionError:
        return False

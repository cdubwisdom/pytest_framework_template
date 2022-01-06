from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def element_exists(driver, by):
    return driver.find_elements(*by).count > 0


# waits for element to exist(or disappear) on web page
def wait_for_element_to_exist(driver, by, seconds=10, negative=False):
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
def find_element_with_wait(driver, by):
    attempts = 0
    while attempts < 2:
        try:
            wait_for_element_to_exist(driver, by)
            return driver.find_element(*by)
        except NoSuchElementException:
            time.sleep(5)
            attempts += 1
    raise NoSuchElementException(f"The element with selector {by} was not located within 2 attempts.")


# sends keyboard actions or text to element
def find_element_and_send_keys(driver, by, text, clear=True, retry=2):
    attempts = 0

    while attempts < retry:
        element = find_element_with_wait(driver, by)

        try:
            if clear:
                element.clear()
            element.send_keys(text)
            break  # if event is successful
        except:
            attempts += 1
            time.sleep(2)


# Clicks on element
def find_element_and_click(driver, by, retry=2):
    attempts = 0

    while attempts < retry:
        element = find_element_with_wait(driver, by)

        try:
            element.click()
            break  # if event is successful
        except:
            attempts += 1
            time.sleep(2)


# Looks for a web alert and accepts it, if no alert found moves on
def accept_alert_if_visible(driver):
    try:
        driver.switch_to.alert.accept()
    except NoAlertPresentException:
        pass


# Selects a dropdown option by its html text from element
def open_and_select_dropdown_by_text(driver, by, option):
    element = Select(find_element_with_wait(driver, by))
    element.select_by_visible_text(option)


# Selects a dropdown option based on html value
def open_and_select_dropdown_by_value(driver, by, option):
    element = Select(find_element_with_wait(driver, by))
    element.select_by_value(option)


# Verifies if text in element matches given string
def does_text_match(driver, by, text):
    element = find_element_with_wait(driver, by)
    try:
        assert element.text.find(text) != -1
        return True
    except AssertionError:
        return False

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import TestLocators


class TestsGoToConstructor:

    def test_go_to_constructor_from_pa(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys("DmitriyOdintsov_08_196@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("Dima08")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCTOR_BUN))

    def test_go_to_main_page_from_pa_logo_click(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys("DmitriyOdintsov_08_196@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("Dima08")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON))

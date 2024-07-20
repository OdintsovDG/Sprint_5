from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import *
from locators import TestLocators


class TestPersonalAreaButton:

    def test_personal_area_true(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys("DmitriyOdintsov_08_196@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys("Dima08")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_PA).click()
        driver.find_element(*TestLocators.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

from data import *
from locators import TestLocators


class TestsConstructorSection:

    def test_section_bun(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUN).click()

    def test_section_sauces(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES).click()

    def test_section_fillings(self, driver):
        driver.get(URL)
        driver.find_element(*TestLocators.CONSTRUCTOR_FILLINGS).click()

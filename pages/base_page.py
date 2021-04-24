import time


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_elements_and_click(self, text, *locator):
        for element in self.driver.find_elements(*locator):
            if element.text == text:
                element.click()
                time.sleep(1)

    def find_elements(self, text, *locator):
        for element in self.driver.find_elements(*locator):
            if element.text == text:
                element.click()
                time.sleep(1)

    def find_element(self, text, *locator):
        for element in self.driver.find_elements(*locator):
            element_text = element.text
            if element_text == text:
                return element_text

    def click_button(self, text, *locator):
        for element in self.driver.find_elements(*locator):
            if element.text == text:
                element.click()
                time.sleep(1)

    def click_button_xpath(self, *locator):
        e = self.driver.find_element(*locator)
        e.click()

    def input_line_xpath(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send_keys(text)

    def input(self, text, send_text, *locator):
        for element in self.driver.find_elements(*locator):
            if element.text == text:
                element.send_keys(send_text)
                time.sleep(1)

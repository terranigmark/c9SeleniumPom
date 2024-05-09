from selenium.webdriver.common.by import By


class WomenCollection:

    women_items = 'grid__item--collection-template'

    def __init__(self, driver):
        self.driver = driver

    def click_on_racer_back_maxi_dress(self):
        driver = self.driver
        items = driver.find_elements(By.CLASS_NAME, self.women_items)
        items[1].click()

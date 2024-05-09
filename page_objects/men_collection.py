from selenium.webdriver.common.by import By


class MenCollection:

    men_items = 'grid__item--collection-template'

    def __init__(self, driver):
        self.driver = driver

    def click_on_slim_fit_dobby_oxford_shirt(self):
        driver = self.driver
        items = driver.find_elements(By.CLASS_NAME, self.men_items)
        items[7].click()
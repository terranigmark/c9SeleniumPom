from selenium.webdriver.common.by import By


class HomePage:

    # Locators de elementos con los que interactuo
    home_url = 'https://madison-island.com/'
    collections_class_name = 'collection-grid-item'
    home_collections_xpath = '//div[@class="collection-grid-item"]'

    def __init__(self, driver):
        self.driver = driver

    def click_on_women_collection(self):
        driver = self.driver
        collections = driver.find_elements(By.CLASS_NAME, self.collections_class_name)
        collections[0].click()

    def click_on_men_collection(self):
        driver = self.driver
        collections = driver.find_elements(By.CLASS_NAME, self.collections_class_name)
        collections[1].click()

    def click_on_accesories_collection(self):
        driver = self.driver
        collections = driver.find_elements(By.CLASS_NAME, self.collections_class_name)
        collections[2].click()

    def assert_home_url(self):
        driver = self.driver
        current_url = driver.current_url
        assert current_url == 'https://madison-island.com/'



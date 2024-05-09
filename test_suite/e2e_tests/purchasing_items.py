from time import sleep
from page_objects.home_page import HomePage
from page_objects.men_collection import MenCollection
from page_objects.women_collection import WomenCollection
from selenium import webdriver


class TestMadison:
    driver = None
    home = None
    men = None
    women = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.home = HomePage(cls.driver)
        cls.men = MenCollection(cls.driver)
        cls.women = WomenCollection(cls.driver)
        cls.driver.get(cls.home.home_url)
        cls.home.assert_home_url()

    def test_comprando_un_vestido(self):
        home = self.home
        women = self.women
        home.click_on_women_collection()
        women.click_on_racer_back_maxi_dress()

    def test_comprando_una_camisa_oxford(self):
        home = self.home
        men_collection = self.men
        home.click_on_men_collection()
        men_collection.click_on_slim_fit_dobby_oxford_shirt()

    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()
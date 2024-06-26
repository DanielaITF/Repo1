from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class JewelryPage(BasePage):

    ENGAGEMENT_RING_CART_BUTTON = (
        By.XPATH, '//*[@id="main"]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[3]/div[2]/button[1]')
    ADD_TO_CART_MESSAGE = (By.CLASS_NAME, 'content')

    JEWELRY_PAGE_URL = 'https://demo.nopcommerce.com/jewelry'

    def navigate_to_jewelry_page(self):
        self.driver.get(self.JEWELRY_PAGE_URL)

    def add_the_engagement_ring_to_cart(self):
        self.click(self.ENGAGEMENT_RING_CART_BUTTON)

    def is_successful_added_to_cart(self):
        return self.is_element_displayed(self.ADD_TO_CART_MESSAGE)

    def get_successful_added_to_cart_message(self):
        return self.get_element_text(self.ADD_TO_CART_MESSAGE)
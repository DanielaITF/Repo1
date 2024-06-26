from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_TEXT = (By.CLASS_NAME, 'page-title')
    CART_EMPTY_TEXT = (By.CLASS_NAME, 'no-data')
    JEWELRY_ITEM = (By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div/div[2]/h2/a')

    CART_PAGE_URL = 'https://demo.nopcommerce.com/cart'

    def navigate_to_cart_page(self):
        self.driver.get(self.CART_PAGE_URL)

    def is_shopping_cart_text_displayed(self):
        return self.is_element_displayed(self.CART_TEXT)

    def get_cart_empty_text(self):
        return self.get_element_text(self.CART_EMPTY_TEXT)

    def get_jewelry_name(self):
        return self.get_element_text(self.JEWELRY_ITEM)
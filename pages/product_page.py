from .locators import BasketLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By



class ProductPage(BasePage):
	def should_be_product_page(self):
		assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear', 'Oops, wrong page'
	def add_to_cart(self):
		btn = self.browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
		btn.click()
	def should_be_the_same_name(self):
		# print(self.browser.find_element(*BasketLocators.ADD_MESSAGE).text)
		# print(self.browser.find_element(By.CSS_SELECTOR, 'div.col-sm-6.product_main h1').text)

		assert self.browser.find_element(*BasketLocators.ADD_MESSAGE).text == self.browser.find_element(By.CSS_SELECTOR, 'div.col-sm-6.product_main h1').text, "There is no such message"
	def should_be_the_same_price(self):
		assert self.browser.find_element(*BasketLocators.PRICE_MESSAGE).text == self.browser.find_element(By.CSS_SELECTOR, '.col-sm-6.product_main p.price_color').text, 'nO SUXH ELEMENT'
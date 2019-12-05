from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, 'form[id="login_form"]')
	REGISTER_FORM = (By.CSS_SELECTOR, 'form[id="register_form"]')

class BasketLocators():
	ADD_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
	ADD_MESSAGE = (By.CSS_SELECTOR, 'div[class="alertinner "] > strong')
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
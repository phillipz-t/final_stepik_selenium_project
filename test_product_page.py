import pytest
from .pages.product_page import ProductPage
from time import sleep
from .pages.locators import BasketLocators
from selenium.webdriver.common.by import By

# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#     page = ProductPage(browser, link)
#     page.open()
#     print(link)
#     page.should_not_be_success_message()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     browser.implicitly_wait(5)
#     page.should_be_the_same_name()
#     page.should_be_the_same_price()
#     # sleep(6666)

# # @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_to_cart()
# 	# sleep(6666)
# 	# page.solve_quiz_and_get_code()

# 	page.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE)


# # @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_guest_cant_see_success_message(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE)



# # @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_message_disappeared_after_adding_product_to_basket(browser):
# 	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_to_cart()
# 	page.is_disappeared(*BasketLocators.SUCCESS_MESSAGE)


def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()	
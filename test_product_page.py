import pytest
from .pages.product_page import ProductPage
from time import sleep


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    print(link)
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(5)
    page.should_be_the_same_name()
    page.should_be_the_same_price()
    # sleep(6666)

    
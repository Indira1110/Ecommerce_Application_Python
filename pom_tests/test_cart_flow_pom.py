from pom.login_page import LoginPage
from pom.products_page import ProductsPage
from pom.cart_page import CartPage


def test_add_item_to_cart(page):
    LoginPage(page).open().login()
    ProductsPage(page).add_first_item_to_cart()

    assert page.locator(".shopping_cart_badge").text_content() == "1"


def test_cart_page_items(page):
    LoginPage(page).open().login()
    ProductsPage(page).add_first_item_to_cart()
    cart_page = CartPage(page)
    cart_page.open()

    assert page.url.endswith("/cart.html")
    assert cart_page.items().count() == 1

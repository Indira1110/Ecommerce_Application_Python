from pom.login_page import LoginPage
from pom.products_page import ProductsPage


def test_products_are_visible(page):
    LoginPage(page).open().login()
    products_page = ProductsPage(page)

    assert products_page.products().count() > 0
    assert products_page.first_price().is_visible()


def test_sort_products(page):
    LoginPage(page).open().login()
    products_page = ProductsPage(page)
    products_page.sort_by("lohi")

    first_price = products_page.first_price().text_content().strip()
    assert first_price == "$7.99"

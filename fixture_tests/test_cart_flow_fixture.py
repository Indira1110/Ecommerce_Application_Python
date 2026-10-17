from fixtures.login_fixture import login_user
from fixtures.cart_fixture import add_item_to_cart


def test_add_to_cart_fixture(page):
    login_user(page)
    add_item_to_cart(page)

    assert page.locator(".shopping_cart_badge").text_content() == "1"


def test_cart_checkout_fixture(page):
    login_user(page)
    add_item_to_cart(page)
    page.locator(".shopping_cart_link").click()
    page.wait_for_url("**/cart.html")
    page.wait_for_selector(".cart_item")

    assert page.url.endswith("/cart.html")
    assert page.locator(".cart_item").count() == 1

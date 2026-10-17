from fixtures.login_fixture import login_user
from fixtures.cart_fixture import add_item_to_cart
from fixtures.checkout_fixture import checkout_item


def test_checkout_fixture(page):
    login_user(page)
    add_item_to_cart(page)
    checkout_item(page)

    assert page.locator("h2.complete-header").text_content() == "Thank you for your order!"

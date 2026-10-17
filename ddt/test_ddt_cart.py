import pytest


@pytest.mark.parametrize(
    "items_to_add,expected_count",
    [
        (1, 1),
        (2, 2),
        (3, 3),
    ],
)
def test_cart_ddt(page, items_to_add, expected_count):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

    for _ in range(items_to_add):
        page.locator("button:has-text('Add to cart')").first.click()

    cart_badge = page.locator(".shopping_cart_badge")
    if expected_count > 0:
        assert cart_badge.text_content() == str(expected_count)
    else:
        assert cart_badge.count() == 0

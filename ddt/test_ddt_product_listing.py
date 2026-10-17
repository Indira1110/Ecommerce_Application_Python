import pytest


@pytest.mark.parametrize(
    "sort_value, expected_first_price",
    [
        ("az", "$29.99"),
        ("za", "$15.99"),
        ("lohi", "$7.99"),
    ],
)
def test_product_list_ddt(page, sort_value, expected_first_price):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

    page.select_option(".product_sort_container", sort_value)
    first_price = page.locator(".inventory_item_price").first.text_content().strip()

    assert first_price == expected_first_price

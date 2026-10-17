import pytest


@pytest.mark.parametrize(
    "first_name,last_name,postal_code",
    [
        ("John", "Doe", "10001"),
        ("Alice", "Smith", "20002"),
    ],
)
def test_checkout_ddt(page, first_name, last_name, postal_code):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

    page.locator("button:has-text('Add to cart')").first.click()
    page.locator(".shopping_cart_link").click()
    page.click("button:has-text('Checkout')")
    page.fill("#first-name", first_name)
    page.fill("#last-name", last_name)
    page.fill("#postal-code", postal_code)
    page.click("#continue")
    page.click("#finish")

    assert page.locator("h2.complete-header").text_content() == "Thank you for your order!"

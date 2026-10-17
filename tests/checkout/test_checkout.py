from tests.conftest import login_user


def test_checkout_happy_path(page):
    login_user(page)

    page.locator("button:has-text('Add to cart')").first.click()
    page.locator(".shopping_cart_link").click()
    page.wait_for_url("**/cart.html")
    page.click("button:has-text('Checkout')")

    page.fill("#first-name", "Indira")
    page.fill("#last-name", "Tester")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    page.click("#finish")
    page.wait_for_selector("h2.complete-header")

    assert page.locator("h2.complete-header").text_content() == "Thank you for your order!"

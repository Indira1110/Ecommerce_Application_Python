def checkout_item(page):
    page.locator(".shopping_cart_link").click()
    page.wait_for_url("**/cart.html")
    page.click("button:has-text('Checkout')")
    page.wait_for_selector("#first-name")
    page.fill("#first-name", "Indira")
    page.fill("#last-name", "Tester")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    page.wait_for_selector("#finish")
    page.click("#finish")
    return page

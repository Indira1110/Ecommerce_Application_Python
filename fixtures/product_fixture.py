def open_products_page(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    try:
        page.wait_for_url("**/inventory.html", timeout=5000)
    except Exception:
        page.wait_for_selector("[data-test='error']", timeout=5000)
    page.wait_for_selector(".inventory_item", timeout=5000)
    return page

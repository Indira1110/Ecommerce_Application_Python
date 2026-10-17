def login_user(page, username="standard_user", password="secret_sauce"):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")

    try:
        page.wait_for_url("**/inventory.html", timeout=5000)
    except Exception:
        page.wait_for_selector("[data-test='error']", timeout=5000)

    return page

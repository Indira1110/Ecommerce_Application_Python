from pom.login_page import LoginPage


def test_logout(page):
    LoginPage(page).open().login()

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    page.wait_for_url("https://www.saucedemo.com/")
    page.wait_for_selector("#login-button", state="visible")

    assert page.url == "https://www.saucedemo.com/"
    assert page.locator("#login-button").is_visible()

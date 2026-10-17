from tests.conftest import login_user


def test_logout_user(page):
    login_user(page)

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    page.wait_for_url("https://www.saucedemo.com/")
    page.wait_for_selector("#login-button", state="visible")

    assert page.url.startswith("https://www.saucedemo.com/")
    assert page.locator("#login-button").is_visible()

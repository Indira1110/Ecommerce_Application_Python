from tests.conftest import login_user


def test_valid_login(page):
    login_user(page)

    assert page.url.endswith("/inventory.html")
    assert page.locator(".title").text_content() == "Products"


def test_invalid_login_shows_error(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    error = page.locator("[data-test='error']")
    assert error.is_visible()
    assert "Epic sadface" in error.text_content()

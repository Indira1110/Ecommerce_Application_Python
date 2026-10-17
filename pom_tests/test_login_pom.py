from pom.login_page import LoginPage


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.open().login()

    assert page.url.endswith("/inventory.html")
    assert page.locator(".title").text_content() == "Products"


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open().login("locked_out_user", "secret_sauce")

    assert login_page.error_message().is_visible()
    assert "Epic sadface" in login_page.error_message().text_content()

import pytest


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
    ],
)
def test_logout_ddt(page, username, password):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    page.wait_for_url("https://www.saucedemo.com/")
    page.wait_for_selector("#login-button", state="visible")

    assert page.url == "https://www.saucedemo.com/"
    assert page.locator("#login-button").is_visible()

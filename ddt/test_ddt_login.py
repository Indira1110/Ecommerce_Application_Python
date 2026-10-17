import pytest


@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("standard_user", "secret_sauce", True),
        ("problem_user", "secret_sauce", True),
        ("standard_user", "wrong_password", False),
        ("wrong_user", "secret_sauce", False),
    ],
)
def test_login_ddt(page, username, password, expected):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")

    if expected:
        page.wait_for_url("**/inventory.html")
        assert page.url.endswith("/inventory.html")
    else:
        assert page.locator("[data-test='error']").is_visible()

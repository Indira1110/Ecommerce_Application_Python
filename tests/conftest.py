import pytest


def login_user(page, username="standard_user", password="secret_sauce"):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", password)
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")
    page.wait_for_selector(".inventory_item", state="visible")
    return page


@pytest.fixture(scope="function")
def before_each_test(page):
    page.set_default_timeout(15000)
    return page

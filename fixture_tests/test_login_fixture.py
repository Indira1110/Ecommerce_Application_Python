from fixtures.login_fixture import login_user


def test_login_fixture(page):
    login_user(page)

    assert page.url.endswith("/inventory.html")
    assert page.locator(".title").text_content() == "Products"


def test_invalid_login_fixture(page):
    page = login_user(page, "locked_out_user", "secret_sauce")

    assert page.locator("[data-test='error']").is_visible()

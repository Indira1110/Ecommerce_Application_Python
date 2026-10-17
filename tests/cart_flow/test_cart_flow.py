from tests.conftest import login_user


def test_add_and_remove_item_from_cart(page):
    login_user(page)

    add_button = page.locator("button:has-text('Add to cart')").first
    add_button.click()

    cart_badge = page.locator(".shopping_cart_badge")
    cart_badge.wait_for(state="visible")
    assert cart_badge.text_content() == "1"

    page.locator("button:has-text('Remove')").first.click()
    page.wait_for_timeout(500)
    assert page.locator(".shopping_cart_badge").count() == 0


def test_cart_page_shows_selected_items(page):
    login_user(page)

    page.locator("button:has-text('Add to cart')").first.click()
    page.locator(".shopping_cart_link").click()
    page.wait_for_url("**/cart.html")
    page.wait_for_selector(".cart_item")

    assert page.url.endswith("/cart.html")
    assert page.locator(".cart_item").count() == 1

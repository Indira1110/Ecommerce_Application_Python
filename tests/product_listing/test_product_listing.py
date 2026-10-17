from tests.conftest import login_user


def test_product_list_is_visible(page):
    login_user(page)

    page.wait_for_selector(".inventory_item")
    product_cards = page.locator(".inventory_item")
    assert product_cards.count() > 0
    assert page.locator(".inventory_item_name").first.is_visible()
    assert page.locator(".inventory_item_price").first.is_visible()


def test_sort_products_by_price_low_to_high(page):
    login_user(page)

    page.select_option(".product_sort_container", "lohi")
    page.wait_for_selector(".inventory_item_price")
    prices = [float(item.text_content().replace("$", "")) for item in page.locator(".inventory_item_price").all()]

    assert prices == sorted(prices)

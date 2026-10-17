from fixtures.product_fixture import open_products_page


def test_products_loaded(page):
    open_products_page(page)

    page.wait_for_selector(".inventory_item")
    assert page.locator(".inventory_item").count() > 0
    assert page.locator(".inventory_item_name").first.is_visible()


def test_product_sort_fixture(page):
    open_products_page(page)
    page.select_option(".product_sort_container", "lohi")
    page.wait_for_selector(".inventory_item_price")

    first_price = page.locator(".inventory_item_price").first.text_content().strip()
    assert first_price == "$7.99"

def add_item_to_cart(page):
    page.wait_for_selector("button:has-text('Add to cart')")
    page.locator("button:has-text('Add to cart')").first.click()
    page.wait_for_selector(".shopping_cart_badge")
    return page

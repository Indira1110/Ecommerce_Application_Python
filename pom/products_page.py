class ProductsPage:
    def __init__(self, page):
        self.page = page

    def products(self):
        self.page.wait_for_selector(".inventory_item")
        return self.page.locator(".inventory_item")

    def add_first_item_to_cart(self):
        self.page.wait_for_selector("button:has-text('Add to cart')")
        self.page.locator("button:has-text('Add to cart')").first.click()
        self.page.wait_for_selector(".shopping_cart_badge")
        return self

    def sort_by(self, value):
        self.page.wait_for_selector(".product_sort_container")
        self.page.select_option(".product_sort_container", value)
        return self

    def first_price(self):
        self.page.wait_for_selector(".inventory_item_price")
        return self.page.locator(".inventory_item_price").first

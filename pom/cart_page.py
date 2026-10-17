class CartPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.wait_for_selector(".shopping_cart_link")
        self.page.locator(".shopping_cart_link").click()
        self.page.wait_for_url("**/cart.html")
        return self

    def items(self):
        self.page.wait_for_selector(".cart_item")
        return self.page.locator(".cart_item")

    def checkout(self):
        self.page.wait_for_selector("button:has-text('Checkout')")
        self.page.click("button:has-text('Checkout')")
        return self

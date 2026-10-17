class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.page.wait_for_selector("#first-name")
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)
        self.page.click("#continue")
        return self

    def finish_order(self):
        self.page.wait_for_selector("#finish")
        self.page.click("#finish")
        return self

    def success_message(self):
        self.page.wait_for_selector("h2.complete-header")
        return self.page.locator("h2.complete-header")

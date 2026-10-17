from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://example.com"

    def open(self):
        self.goto(self.URL)
        return self

    def main_text(self):
        return self.page.locator("body")

class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.wait_for_selector("#login-button")
        return self

    def login(self, username="standard_user", password="secret_sauce"):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
        self.page.wait_for_load_state("networkidle")
        return self

    def error_message(self):
        return self.page.locator("[data-test='error']")

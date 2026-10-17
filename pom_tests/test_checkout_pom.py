from pom.login_page import LoginPage
from pom.products_page import ProductsPage
from pom.cart_page import CartPage
from pom.checkout_page import CheckoutPage


def test_checkout_success(page):
    LoginPage(page).open().login()
    ProductsPage(page).add_first_item_to_cart()
    CartPage(page).open().checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("Indira", "Tester", "12345")
    checkout_page.finish_order()

    assert checkout_page.success_message().text_content() == "Thank you for your order!"

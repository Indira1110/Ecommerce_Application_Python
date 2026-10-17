from pages.home_page import HomePage


def test_example_domain_loads(page):
    home = HomePage(page)
    home.open()

    assert "Example Domain" in home.get_title()
    body_text = home.main_text().inner_text()
    assert "This domain is for use in documentation examples" in body_text

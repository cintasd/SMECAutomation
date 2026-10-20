from pages.home_page import HomePage

def test_homepage_loads(page):
    home = HomePage(page)
    home.open_homepage()

    assert home.get_heading() == "Learn to code without getting stuck."
    assert page.title() == "Learn to code without getting stuck | Dev4Hub"


def test_user_can_navigate_to_login_page(page):
    home = HomePage(page)
    home.open_homepage()


def test_user_can_open_python_course(page):
    home = HomePage(page)
    home.open_homepage()

    home.click_course("Python")

    assert page.url.endswith("/python")

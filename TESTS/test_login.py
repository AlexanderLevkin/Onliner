from PAGES.main_page import MainPage


def test_login(brows):
    MainPage(brows).enter_to_account()
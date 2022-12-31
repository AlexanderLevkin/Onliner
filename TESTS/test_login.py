from PAGES.authorization_page import MainPage
from PAGES.item_page import ItemPage


def test_login(brows):
    MainPage(brows).enter_to_account()
    ItemPage(brows).get_item_to_cart()

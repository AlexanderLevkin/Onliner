from PAGES.authorization_page import MainPage
from PAGES.filter_phone_item import FilterPage
from PAGES.item_phone_page import ItemPage


def test_login(brows):
    # MainPage(brows).enter_to_account()
    ItemPage(brows).get_item()
    FilterPage(brows).get_filter_and_add_to_cart()

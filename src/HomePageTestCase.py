from src.common.Pages import HomePage
from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators


class HomePageTest(BrowserTestCase):
    def test_homepage_loaded(self):
        """ Asserts the home page title is correct
        """
        self.home_page = HomePage(self.driver)
        self.assertIn(TestData.HOME_PAGE_TITLE, self.home_page.driver.title)

    def test_homepage_search_toggle(self):
        """Asserts the search toggle is present on home page
        """
        self.home_page = HomePage(self.driver)
        self.assertTrue(self.home_page.is_enabled(
            Locators.SEARCH_TOGGLE))

    def test_homepage_top_cards(self):
        """ Asserts both air forecasts cards are loaded
        """
        self.home_page = HomePage(self.driver)
        cards_list = self.home_page.get_elements(Locators.HOME_CARD)
        first_two_cards = [card.text for card in cards_list[:2]]
        self.assertEqual(first_two_cards, TestData.TOP_CARDS)

    def test_homepage_top_menu_data_link(self):
        """ Checks for the Data link in the header
        """
        self.home_page = HomePage(self.driver)
        self.home_page.is_enabled(Locators.DATA_LINK)
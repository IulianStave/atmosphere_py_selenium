from src.common.Pages import DataPage
from src.common.common import BrowserTestCase
from src.data.TestData import TestData
from src.data.Locators import Locators


class DataCatalogueTest(BrowserTestCase):
    def test_access_the_catalogue(self):
        """ Clicks on the catalogue page link
        """
        self.data_page = DataPage(self.driver)
        catalogue_link = self.data_page.is_enabled(
            Locators.CATALOGUE_LINK)
        catalogue_link.click()
        self.assertEqual(self.driver.current_url, TestData.CATALOGUE_URL)

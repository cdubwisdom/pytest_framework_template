import pytest
from scr.tests.writer_helper import Writer  # use only for developing new test methods


@pytest.mark.usefixtures('chrome_driver_init')
class TestFailExamples:
    def test_should_not_display_irrelevant_results_from_web_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I enter a query in search field
        # And: I click 'Search' button
        self.home_page.web_search(search_query='cookies')

        # Then: I can see a list of relevant web pages
        assert self.web_results_page.is_expected_result_url_listed(search_result='https://docs.pytest.org/') is True # Test fails because this should be False

    @pytest.mark.xfail
    def test_should_not_display_irrelevant_results_from_img_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I click on 'Images' Tab
        # And: I enter a query in search field
        # And: I hit 'Enter' on keyboard (Image Search Page has no button)
        self.home_page.img_search(search_query='cookies')

        # Then: I can see relevant images
        assert self.img_results_page.is_expected_result_img_listed(search_result='pytest · PyPI') is True # Test fails because this should be False

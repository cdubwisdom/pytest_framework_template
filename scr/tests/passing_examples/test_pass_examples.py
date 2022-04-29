import pytest
from scr.tests.writer_helper import Writer  # use only for developing new test methods


@pytest.mark.usefixtures('chrome_driver_init')
class TestPassExamples:
    def test_should_display_relevant_result_from_web_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I enter a query in search field
        # And: I click 'Search' button
        self.home_page.web_search(search_query='pytest')

        # Then: I can see a list of relevant web pages
        assert self.web_results_page.is_expected_result_url_listed(search_result='https://pytest.org/') is True

    def test_should_display_relevant_result_from_img_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I click on 'Images' Tab
        # And: I enter a query in search field
        # And: I hit 'Enter' on keyboard (Image Search Page has no button)
        self.home_page.img_search(search_query='pytest')

        # Then: I can see relevant images
        assert self.img_results_page.is_expected_result_img_listed(search_result='Pytest - Wikipedia') is True

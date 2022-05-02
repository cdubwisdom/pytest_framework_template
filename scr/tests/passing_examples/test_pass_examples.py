import pytest
from scr.tests.writer_helper import Writer  # use only for developing new test methods
'''
Feature: Search the internet
    In order to find information
    As a user
    I want to see relevant content
'''


@pytest.mark.usefixtures('chrome_driver_init')
class TestPassExamples:
    # Scenario: Should be able to see relevant info from web search
    def test_should_display_relevant_result_from_web_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I give a query to the search field
        # And: I initiate the search
        self.home_page.web_search(search_query='pytest')

        # Then: I can see a list of relevant web pages
        assert self.web_results_page.is_expected_result_url_listed(search_result='https://pytest.org/') is True

    # Scenario: Should be able to see relevant image from image search
    def test_should_display_relevant_result_from_img_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I navigate to the 'Images' Tab
        # And: I give a query to the search field
        # And: I initiate the search
        self.home_page.img_search(search_query='pytest')

        # Then: I can see relevant images
        assert self.img_results_page.is_expected_result_img_listed(search_result='Pytest - Wikipedia') is True

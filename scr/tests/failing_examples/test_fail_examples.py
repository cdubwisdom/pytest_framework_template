import pytest
from scr.tests.writer_helper import Writer  # use only for developing new test methods

'''
Feature: Search the internet
    In order to find information
    As a user
    I want to see ONLY relevant content
'''


@pytest.mark.usefixtures('chrome_driver_init')
class TestFailExamples:
    # Scenario: Should not see irrelevant info from web search
    def test_should_not_display_irrelevant_results_from_web_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I give a query to the search field
        # And: I initiate the search
        self.home_page.web_search(search_query='cookies')

        # Then: I can see a list of ONLY relevant web pages
        assert self.web_results_page.is_expected_result_url_listed(
            search_result='https://docs.pytest.org/') is True  # Test fails because this should be False

    @pytest.mark.xfail
    # Scenario: Should not see irrelevant images from image search
    def test_should_not_display_irrelevant_results_from_img_search(self):
        # Given: I am on the Google Search Page
        # Defined in conftest.py

        # When: I click on 'Images' Tab
        # And: I give a query to the search field
        # And: I initiate the search
        self.home_page.img_search(search_query='cookies')

        # Then: I can see a list of ONLY relevant web pages
        assert self.img_results_page.is_expected_result_img_listed(
            search_result='pytest · PyPI') is True  # Test fails because this should be False

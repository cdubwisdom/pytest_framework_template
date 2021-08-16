import pytest
from page_objects.example_google_home import GoogleHome
from page_objects.example_web_result_page import WebResults


@pytest.mark.usefixtures('chrome_driver_init')
class TestExample:
    def test_example(self):
        #Perform Web Search
        self.home_page.web_search(search_query='pytest')

        #Verify expected result is listed
        assert self.results_page.is_expected_result_url_listed(search_result='https://pytest.org/') is True
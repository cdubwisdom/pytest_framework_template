import pytest


@pytest.mark.usefixtures('chrome_driver_init')
class TestExample:
    def test_example(self):
        # Perform Web Search
        self.home_page.web_search(search_query='pytest')

        # Verify expected result is listed
        assert self.results_page.is_expected_result_url_listed(search_result='https://docs.pytest.org/') is True

    def test_fail_example(self):
        # Perform Web Search
        self.home_page.web_search(search_query='cookies')

        # Verify expected result is listed
        assert self.results_page.is_expected_result_url_listed(search_result='https://docs.pytest.org/') is True

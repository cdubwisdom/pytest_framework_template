import pytest


@pytest.mark.usefixtures('chrome_driver_init')
class TestFailExamples:
    def test_web_example(self):
        # Perform Web Search
        self.home_page.web_search(search_query='cookies')

        # Verify expected result is listed
        assert self.web_results_page.is_expected_result_url_listed(search_result='https://docs.pytest.org/') is True

    @pytest.mark.xfail
    def test_img_search(self):
        # Perform Image Search
        self.home_page.img_search(search_query='cookies')

        # Verify expected result is listed
        assert self.img_results_page.is_expected_result_img_listed(search_result='pytest · PyPI') is True

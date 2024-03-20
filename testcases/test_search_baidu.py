import pytest

from page.search_baidu import *
import time


class TestSearchBaiDu:
	url = "http://www.baidu.com"

	@pytest.mark.usefixtures('get_driver')
	def test_search_info(self, get_driver):
		try:
			search_run_method(url=TestSearchBaiDu.url, string="刀妹", driver=get_driver)
			time.sleep(3)
			assert '刀妹' in get_driver.page_source
		except Exception as e:
			raise e

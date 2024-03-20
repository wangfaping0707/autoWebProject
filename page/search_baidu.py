import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Base.base_page import BasePage


class SearchBaiDu(BasePage):
	# 定位百度输入框
	input_box = (By.ID, 'kw')
	# 定位百度页面的点击按钮
	click_button = (By.XPATH, '//*[@id="su"]')

	# 输入要百度的信息
	def search(self, search_string):
		# self.locator_element(*self.input_box).send_keys(search_string)
		self.search_content(SearchBaiDu.input_box, search_string)
		self.driver.get_screenshot_as_file("b.png")

	# 点击"百度一下"按钮
	def click_method(self):
		self.locator_element(SearchBaiDu.click_button).click()
		time.sleep(3)


# 组装运行方法供外部简便调用

def search_run_method(url, string, driver):
	sbd = SearchBaiDu(driver)
	sbd.open_browser(url)
	sbd.search(string)
	time.sleep(2)
	sbd.click_method()

# if __name__ == '__main__':
# 	text = '刀锋之影'
# 	url = "http://www.baidu.com"
# 	driver = webdriver.Chrome()
# 	sbd = SearchBaiDu(url, driver)
# 	sbd.open_browser()
# 	sbd.search(text)
# 	sbd.click_method()

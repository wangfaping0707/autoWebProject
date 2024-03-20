import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

"""
23、关闭浏览器中quit和close的区别？
简单来说，两个都可以实现退出浏览器session功能：
Close：是关闭你当前聚焦的tab页面，而quit是关闭全部浏览器tab页面，并退出浏览器session。
知道这两个区别，我们就知道quit一般用在结束测试之前的操作，close用在执行用例过程中关闭某一个页面的操作。

浏览器更新：设置自动下载对应的驱动
"""


@pytest.fixture(scope='function')
def get_driver():
	# 可以自动下载对应的浏览器更新驱动
	# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
	driver = webdriver.Chrome()
	yield driver
	driver.quit()
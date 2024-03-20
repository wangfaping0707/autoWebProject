import time

from selenium import webdriver


# 定义页面的基础类，所有的页面都需要继承这个基础类
class BasePage(object):
	# driver = webdriver.Chrome()

	def __init__(self, driver):
		"""
		初始化基础类
		:param driver:
		"""
		self.driver = driver

	def open_browser(self, url):
		"""
		启动浏览器，访问指定页面
		:param url: 需要访问的页面地址
		:return:
		"""
		self.driver.get(url)
		self.driver.maximize_window()

	def locator_element(self, locator):
		"""
		定位元素：
		:param locator: 定位方式以及对应 定位的值以元组形式传入，*号表示这个元组不能当成一个参数使用，需要进行序列解包操作
		:return:返回查找的元素
		"""
		ele = self.driver.find_element(*locator)
		return ele

	def search_content(self, locator, content):
		"""
		定位输入框 并输入对应的内容进行搜索
		:param content: 要查询的信息
		:param element: 定位方式以及对应 定位的值以元组形式传入，*号表示这个元组不能当成一个参数使用，需要进行序列解包操作
		:return:
		"""
		self.locator_element(locator).send_keys(content)

	def quit(self):
		"""
		关闭浏览器
		:return:
		"""
		time.sleep(2)
		self.driver.quit()

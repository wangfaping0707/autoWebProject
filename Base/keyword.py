import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def open_browser(b_type, url):
	"""
	浏览器运行初始化
	:param b_type: 要启动的浏览器类型
	:param url: 要访问的页面url
	:return:
	"""
	if b_type == "chrome":
		driver = webdriver.Chrome()
		print("starting for Chrome")
	elif b_type == "firefox":
		driver = webdriver.Firefox()
		print("starting for Firefox")
	elif b_type == "ie":
		driver = webdriver.Ie()
		print("starting for Ie")
	driver.maximize_window()
	driver.get(url)
	driver.implicitly_wait(5)
	return driver


class WebUiInit(object):
	# 初始化 WebUiInit 类
	def __init__(self, b_type, url):
		self.driver = open_browser(b_type, url)

	def quit(self):
		"""
		关闭浏览器
		:return:
		"""
		self.driver.quit()

	def search_content(self, content, locator_type, locator_value):
		"""
		依据不同的定位方法，进行输入操作
		:param content: 要搜索的内容
		:param locator_type: 定位方式
		:param locator_value:  定位方式对应的值
		:return:
		"""
		if locator_type == 'xpath':
			self.driver.find_element(By.XPATH, locator_value).send_keys(content)
		elif locator_type == 'id':
			self.driver.find_element(By.ID, locator_value).send_keys(content)
		elif locator_type == 'name':
			self.driver.find_element(By.NAME, locator_value).send_keys(content)
		elif locator_type == 'text':
			self.driver.find_element(By.LINK_TEXT, locator_value).send_keys(content)

	def click(self, locator_type, locator_value):
		"""
		依据不同的定位方法，进行点击操作
		:param locator_type: 定位方式
		:param locator_value:  定位方式对应的值
		:return:
		"""
		if locator_type == 'xpath':
			self.driver.find_element(By.XPATH, locator_value).click()
		elif locator_type == 'id':
			self.driver.find_element(By.ID, locator_value).click()
		elif locator_type == 'name':
			self.driver.find_element(By.NAME, locator_value).click()
		elif locator_type == 'text':
			self.driver.find_element(By.LINK_TEXT, locator_value).click()

	def time_sleep(self, seconds):
		"""
		定义  强制等待
		:param seconds:
		:return:
		"""
		time.sleep(seconds)

	def implic_wait(self, seconds):
		"""
		定义  隐私等待
		:param seconds:
		:return:
		"""
		self.driver.implicitly_wait(seconds)

	def switch_to_new_current(self):
		"""
		切换至新窗体
		:return:
		"""
		handles = self.driver.window_handles
		self.driver.switch_to.window(handles[1])

	def close_old_current(self):
		"""关闭 旧窗体"""
		self.driver.close()

	def switch_to_old_current(self):
		"""切换到旧窗体"""
		handles = self.driver.window_handles
		self.driver.switch_to.window(handles[0])

	def switch_to_new_current_and_close_old_current(self):
		"""切换到新窗口，并关闭旧窗口"""
		handles = self.driver.window_handles
		self.driver.close()
		self.driver.switch_to.window(handles[1])

	def click(self, locator_type, locator_value, text):
		"""
		获取元素文本内容 进行断言校验
		:param locator_type: 定位方式
		:param locator_value:  定位方式对应的值
		:return:
		"""
		if locator_type == 'xpath':
			element_text = self.driver.find_element(By.XPATH, locator_value).text
		elif locator_type == 'id':
			element_text = self.driver.find_element(By.ID, locator_value).text
		elif locator_type == 'name':
			element_text = self.driver.find_element(By.NAME, locator_value).text
		elif locator_type == 'text':
			element_text = self.driver.find_element(By.LINK_TEXT, locator_value).text

		if element_text == text:
			print(f'断言通过：{element_text} VS {text}')
		else:
			print(f'断言失败，fail_info: {element_text} VS {text}')

	def switch_to_iframe(self, locator_type, locator_value, text):
		"""
		切换到iframe窗体
		:param locator_type: 定位方式
		:param locator_value:  定位方式对应的值
		:return:
		"""
		if locator_type == 'xpath':
			self.driver.switch_to.frame(self.driver.find_element(By.XPATH, locator_value))
		elif locator_type == 'id':
			self.driver.switch_to.frame(self.driver.find_element(By.ID, locator_value))
		elif locator_type == 'name':
			self.driver.switch_to.frame(self.driver.find_element(By.NAME, locator_value))

	def switch_to_default(self):
		"""切换回 默认窗体"""
		self.driver.switch_to.default_content()


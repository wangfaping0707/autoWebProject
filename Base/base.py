import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
	driver = webdriver.Chrome()
	driver.find_element()

	def __init__(self, driver):
		self.driver = driver

	def open_browser(self, url):
		"""
		启动浏览器，访问指定页面
		:param url: 需要访问的页面地址
		:return:
		"""
		self.driver.get(url)
		self.driver.maximize_window()

	# 使用显示等待  查找元素
	def base_find_element(self, locator, timeout=20, poll_frequency=0.5):
		"""
		功能：封装查找页面元素的方法，并添加显示等待，可设置默认查找元素等待时间
		:param locator:  定位方式以及对应 定位的值以元组形式传入，*号表示这个元组不能当成一个参数使用，需要进行序列解包操作
		:param timeout: 查找元素显示等待 需要传入等待的时间，不传，默认等待30秒
		:param poll_frequency: 查询的频率
		:return: 返回查找的元素
		"""
		ele = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
			lambda x: x.find_element(*locator))
		return ele

	# 点击元素
	def base_click(self, locator):
		"""
		功能：调用查找元素方法之后，对查找到的元素进行点击
		:param locator: 定位方式以及对应 定位的值以元组形式传入，*号表示这个元组不能当成一个参数使用，需要进行序列解包操作
		:return:
		"""
		self.base_find_element(locator).click()

	# 输入内容方法
	def base_input(self, locator, content):
		"""
		功能：输入框中，先清空输入框，在输入要查找的内容
		:param locator: 定位方式以及对应 定位的值以元组形式传入，*号表示这个元组不能当成一个参数使用，需要进行序列解包操作
		:param content: 要输入的内容
		:return:
		"""
		ele = self.base_find_element(locator)
		# 先清空输入框
		ele.clear()
		# 输入内容
		ele.send_keys(content)

	# 获取文本方法
	def base_get_text(self, locator):
		"""
		功能：返回查找到的元素，对应的文本信息
		:param locator:
		:return:
		"""
		res = self.base_find_element(locator).text
		return res

	# 页面截图方法
	def base_get_image(self, path="./{}.png".format(time.strftime('%Y-%m-%d-%H_%M_%S'))):
		"""
		功能：对测试过程中，出现异常的页面进行截图
		:param path: 保存截图的目录路径及对应的图片名，path有默认值，也可自己传入自定义路径
		:return:
		"""
		self.driver.get_screenshot_as_file(path)

	# 获取元素 特定属性的值 ,比如<input value='1'></input>
	def base_get_attribute_value(self, loc, attribute):
		"""
		功能： 获取元素 特定属性的值 ,比如   <input value='1'></input>  这个标签元素，属性value对应的值
		:param loc:
		:param attribute: 要获取的值对应的属性名称
		:return:  返回获得属性值
		"""
		return self.base_find_element(loc).get_attribute(attribute)

	# 封装：判断查找的元素是否存在
	def base_element_if_exist(self, loc):
		try:
			self.base_find_element(loc, timeout=5)
			# 查找到元素，返回True
			return True
		except AssertionError:
			# 没有找到元素，返回False
			return False

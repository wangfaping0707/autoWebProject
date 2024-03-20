import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class UtilsDriver:
	# 避免直接调用，将变量进行私有化
	__driver = None

	# 获取driver对象
	@classmethod
	def get_web_driver(cls):
		"""
		使用单例设计模式：当用户调用这个方法的时候，先判断有没有已经生成的实例，如果有，直接返回
		如果没有，在生成，然后返回
		:return:
		"""
		if cls.__driver is None:
			cls.__driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
			cls.__driver.maximize_window()
			return cls.__driver
		else:
			return cls.__driver

	@classmethod
	def quit_driver(cls):
		if cls.__driver is not None:
			cls.__driver.close()
			cls.__driver.quit()
			cls.__driver = None

	# 自定义等待元素方法
	def find_element_wait(self, __driver, *locator, num):
		"""
		自定义元素查找等待函数
		:param __driver: 浏览器驱动
		:param locator: 元组，定位方式以及对应的值
		:param num: 最多等待的时间，单位为秒数
		:return: 返回查找的元素
		"""
		start_time = time.time()
		while time.time() < start_time + num:
			time.sleep(0.3)
			try:
				return self.__driver.find_element(*locator)
			except:
				print('元素未找到。。。')
		return __driver.find_element(*locator)

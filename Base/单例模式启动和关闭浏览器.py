from selenium import webdriver


class GetDriver:
	# 将浏览器驱动设置为类变量
	driver = None

	url = "http://localhost"

	# 获取浏览器driver
	@classmethod
	def get_brower_driver(cls):
		if cls.driver is None:
			cls.driver = webdriver.Chrome()
			# 最大化浏览器窗口
			cls.driver.maximize_window()
			# 打开浏览器
			cls.driver.get(url=cls.url)
		return cls.driver

	# 退出driver
	@classmethod
	def quit_driver(cls):
		if cls.driver:
			cls.driver.quit()
			# 注意，此处有个坑，关闭浏览器之后，必须要把driver置空
			cls.driver = None

import page
from Base.base import Base


class PageLogin(Base):
	# 点击登录链接
	def page_click_login_link(self):
		self.base_click(page.login_link)

	# 输入用户名
	def page_input_username(self, username):
		self.base_input(page.login_username, username)

	# 输入密码
	def page_input_password(self, pwd):
		self.base_input(page.login_pwd, pwd)

	# 输入验证码
	def page_input_verify_code(self, code):
		self.base_input(page.login_verify_code, code)

	# 点击登录按钮
	def page_click_login_btn(self):
		self.base_click(page.login_btn)

	# 获取异常提示信息
	def page_get_error_info(self):
		return self.base_get_text(page.login_error_info)

	# 点击异常信息提示框的 确定按钮，关闭弹框
	def page_click_error_btn_ok(self):
		self.base_click(page.login_error_btn_ok)

	# 对错误页面进行截图
	def page_get_screenshot(self):
		self.base_get_image()

	# # 将操作元素的方法进行组合，以供外部调用：即业务层进行调用
	# def page_login(self, username, pwd, code):
	# 	self.page_input_username(username)
	# 	self.page_input_password(pwd)
	# 	self.page_input_verify_code(code)
	# 	# 点击登录按钮
	# 	self.page_click_login_btn()

	# 点击 安全退出 按钮-》退出登录状态
	def page_click_logout(self):
		self.base_click(page.login_logout)

	# 判断是否登录成功
	def page_is_login_success(self):
		return self.base_element_if_exist(page.login_logout)





# 对登录页面进行登录操作
def page_login(url, driver, data):
	username, pwd, code, expect_result = data
	po = PageLogin(driver)
	po.open_browser(url)
	# 点击登录按钮，跳转到登录页面
	po.page_click_login_link()
	# 用户名输入框输入数据
	po.page_input_username(username)
	# 密码输入框输入数据
	po.page_input_password(pwd)
	# 验证码输入框输入数据
	po.page_input_verify_code(code)
	# 点击登录按钮，进行登录操作
	po.page_click_login_btn()
	# 获取弹框提示信息
	msg = po.page_get_error_info()
	# 进行判断，如果页面登录报错，则进行截图
	try:
		# 断言
		assert msg == expect_result
	except AssertionError:
		po.page_get_screenshot()
		raise

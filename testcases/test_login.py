import pytest

from page.page_login import *


def get_data():
	return [("13800001234", '123456', '8888', '账号不存在！'), ("13800001111", '123123', '8888', '密码错误！')]


class TestLogin:
	url = 'http://www.baidu.com'

	# 登录页面进行测试,并进行参数化登录
	@pytest.mark.parametrize('data', get_data())
	def test_login_page(self, data, get_driver):
		print(f'data: {data}')
		# 调用登录方法
		page_login(url=TestLogin.url, data=data, driver=get_driver)

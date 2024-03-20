"""以下为登录页面：元素定位方式及信息"""
# 登录链接:页面上有一个登录按钮，点击之后，页面就会跳转到登录页
from selenium.webdriver.common.by import By

login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名输入框
login_username = By.ID, "username"
# 密码输入框
login_pwd = By.ID, "password"
# 验证码输入框
login_verify_code = By.ID, "verify_code"
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 获取异常文本信息
login_error_info = By.CSS_SELECTOR, ".layui-layer-content"
# 点击异常提示框 确定按钮
login_error_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出按钮
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"
"""以下为订单页面：元素定位方式及信息"""

"""以下为支付页面：元素定位方式及信息"""

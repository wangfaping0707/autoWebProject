# 先导入后续要使用的包
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# 创建一个webDriver的实例，接下来的所有操作都是在该实例上进行，以Chrome实例为例
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 访问百度网址
driver.get("https://www.baidu.com/")
title = driver.title
print(f'当前网页标题：{title}')
# 通过元素id找到对应元素并输入值进行搜索；此处为在百度搜索框输入selenium并点击查询
driver.find_element(By.ID, "kw").send_keys("阿卡丽")
driver.find_element(By.ID, "su").click()
time.sleep(2)
# 对访问过程进行截图,图片名称动态变化为时间戳f
driver.get_screenshot_as_file("./{}.png".format(time.strftime('%Y-%m-%d-%H_%M_%S')))
print('djdjdjd')
# driver.get_screenshot_as_file('./aa.png')


# print(f'变动的时间为：{time.strftime("%Y-%m-%d %H:%M:%S")}')
# # 基于id定位:百度输入框
# driver.find_element(By.ID, "kw")
# # 基于name定位:百度输入框
# driver.find_element(By.NAME, "wd")
# # 基于class name定位:百度输入框
# driver.find_element(By.CLASS_NAME, "s_ipt")
# # 基于tag name定位:百度输入框
# driver.find_element(By.TAG_NAME, "input")
#
# # 精确文本定位
# driver.find_element(By.LINK_TEXT, "新闻")
# # 模糊文本定位
# driver.find_element(By.PARTIAL_LINK_TEXT, "新")
#
# # 基于css定位
# driver.find_element(By.CSS_SELECTOR, "#su")
#
# # 模拟鼠标操作
# action = ActionChains(driver)
# # 模拟鼠标右击
# action.context_click()

# try:
# 	pass
# except Exception as e:
# 	raise e
# finally:
# 	pass


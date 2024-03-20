from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # WebDriverWait注意大小写
from selenium.webdriver.common.by import By


def testdd():
	driver = webdriver.Chrome()
	driver.get('http://www.baidu.com')
	try:
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')), '没有定位到哎。。。')
		element.send_keys('123')
		driver.find_element(By.ID, 'su').click()
	except Exception as message:
		print('元素定位报错%s' % message)
	finally:
		pass

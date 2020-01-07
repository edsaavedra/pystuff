from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.request

driver = webdriver.Chrome("D:/Documents/UtilityApps/chromedriver.exe")

urls = []
title = ''

def geturls():
	driver.get("")
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'download')))
	title = driver.find_element_by_css_selector('.course-sidebar > h2').text.replace(':', '')
	for i, course in enumerate(driver.find_elements_by_css_selector('.section-list a.item'), ):
		try:
			course.click()
			time.sleep(5)
			url = driver.find_element_by_css_selector('.download').get_attribute('href')
			name = f'{i} - {driver.find_element_by_id("lecture_heading").text.strip()}'
			print(f'title: {name} url: {url}')
			urls.append([url, name])
			print('ok')
		except Exception as e:
			print(e)
			pass
	with open(f'{title}.txt','w') as f:
		for item in urls:
			f.write("%s\n" % item)

def logIn():
    driver.get('https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
        driver.find_element_by_id('user_email').send_keys('eduardosaavedram@live.com')
        driver.find_element_by_id('user_password').send_keys('eds1016')
        driver.find_element_by_css_selector('.btn-md.login-button').click()
        geturls()
    finally:
        pass
logIn()
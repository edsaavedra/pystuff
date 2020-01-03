import urllib.request
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:/Documents/UtilityApps/chromedriver.exe")

def scrap(url):
	try:
		driver.get(url)
		bwall = driver.find_element_by_css_selector('#bigwall img')
		src = bwall.get_attribute('src')
		urllib.request.urlretrieve(src, 'photos/' + src.rsplit('/', 1)[-1])
		time.sleep(1)
		driver.find_element_by_css_selector('#leftblock .right a:nth-child(2)').click()
		print(src, driver.current_url)
		scrap(driver.current_url)
	except Warning:
		print('err', Warning)
		scrap(driver.current_url)
		pass


scrap("")

# try:
# 	driver.find_element_by_id('username').send_keys('edsaavedram')
# 	driver.find_element_by_id('password').send_keys('eds1016')
# 	driver.find_element_by_css_selector('.signin-button button[name="submit"]').click()
# 	driver.find_element_by_css_selector('a.topbar-icon').click()
# 	imgs = driver.find_elements_by_css_selector('.Post-item-media img')
# 	for img in imgs:
# 		src = img.get_attribute('src')
# 		urllib.request.urlretrieve(src, 'photos/' + src.split('/')[3].split('.')[0] + '.jpg')
# except Warning:
# 	print('err', Warning)
# 	pass
#driver.close()


# today = datetime.datetime.now()
# month = int(today.strftime('%m'))
#
#
# def get_next_month(m):
# 	return m + 1 if m < 12 else 1
#
#
# def reserve(scenario='reg'):
# 	try:
# 		driver.get('https://www.southwest.com/air/booking')
# 		driver.find_element_by_id('originationAirportCode').send_keys('hou')
# 		driver.find_element_by_id('destinationAirportCode').send_keys('mex' if scenario == 'int' else 'dall')
# 		departure = driver.find_element_by_id('departureDate')
# 		arrival = driver.find_element_by_id('returnDate')
# 		departure.clear()
# 		departure.send_keys(str(get_next_month(month)) + '/10')
# 		arrival.clear()
# 		arrival.send_keys(str(get_next_month(month)) + '/25')
# 		driver.find_element_by_id('form-mixin--submit-button').click()
#
# 		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'air-booking-fares-0-1'))).click()
# 		driver.find_element_by_css_selector('.air-booking-jump-link').click()
# 		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'air-booking-fares-1-1'))).click()
# 		driver.find_element_by_css_selector('.air-booking-jump-link').click()
# 	except Warning:
# 		print('err', Warning)
# 		driver.close()
# 		pass
#
# reserve()

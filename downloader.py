from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("D:/Documents/UtilityApps/chromedriver.exe")
urls = []

def geturls():
    driver.get('https://codewithmosh.com/courses/417695/lectures/6781576')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'download')))
    title = driver.find_element_by_id('lecture_heading').text
    for course in driver.find_elements_by_css_selector('.section-list a.item'):
        title = driver.find_element_by_id('lecture_heading').text
        print('title: ' + title)
        course.click()
        time.sleep(3)
        urls.append(driver.find_element_by_css_selector('.download').get_attribute('href'))
        print(urls)

def logIn():
    driver.get('https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1')
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
        driver.find_element_by_id('user_email').send_keys('eduardosaavedram@live.com')
        driver.find_element_by_id('user_password').send_keys('eds1016')
        driver.find_element_by_css_selector('.btn-md.login-button').click()
        wait = WebDriverWait(driver, 10)
        geturls()
    finally:
        pass
logIn()
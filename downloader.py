from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import progressbar
import time
import urllib.request

driver = webdriver.Chrome("D:/Documents/UtilityApps/chromedriver.exe")
pbar = None

def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

def downloadVids(videoUrl, name):
    urllib.request.urlretrieve(videoUrl, name, show_progress)

def geturls():
    driver.get('https://codewithmosh.com/courses/293204/lectures/4509750')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'download')))
    for course in driver.find_elements_by_css_selector('.section-list a.item'):
        try:
            course.click()
            time.sleep(5)
            timest = str(int(datetime.timestamp(datetime.now())))
            title = driver.find_element_by_id('lecture_heading').text.strip()
            print('title: ' + title)
            downloadVids(driver.find_element_by_css_selector('.download').get_attribute('href'), 'node/' + timest + ' - ' + title + '.mp4')
            print('ok')
        except Exception as e:
            print(e)
            pass

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
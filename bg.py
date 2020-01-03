import ctypes
import json
import os
import requests
import urllib

session = requests.Session()
response = session.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
imgUrl = 'https://bing.com' + str(json.loads(response.text).get("images")[0].get("startdate")) + 'jpg'
imgName = imgUrl.rsplit("/", 1)[1]

try:
	urllib.request.urlretrieve(imgUrl, './photos/' + imgName)
	ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd() + '\\photos\\' + imgName, 0)
	print(os.getcwd() + '\\photos\\' + imgName)
except ConnectionError:
	print(ConnectionError)
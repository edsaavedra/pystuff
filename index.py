import urllib.request
import requests
import bs4
import re

req = requests.get('https://www.primejailbait.com/gallery/')
soup = bs4.BeautifulSoup(req.text, 'html.parser')

# def loader(r):
#     r = 'https://www.primejailbait.com' + soup.select('.thlink')[0].get('href') if r == '' else r
#     main = requests.get(r)
#     mainsoup = bs4.BeautifulSoup(main.text, 'html.parser')
#     url = mainsoup.select('#bigwall img')[0].get('src')
#     print(url)
#     urllib.request.urlretrieve(url, 'photos/' + url.rsplit('/', 1)[-1])
#     loader('https://www.primejailbait.com' + mainsoup.select('.right a')[0].get('href'))
#
#
# loader('')
sc = {"page": 1, "last": 0}


def scrap():
    for idx, link in enumerate(soup.select('.thlink img')):
        selector = link.get('src').split('/')[5:7]
        sc.last = re.findall('\d+', soup.select('.thlink')[idx].get('href').rsplit('/', 1)[0])[0]
        urllib.request.urlretrieve('https://pjb.primecdn.net/pics/original/' + selector[0] + '/' + selector[1], 'photos/' + selector[1])
    sc.page += 1
    print(sc)

# 'https://www.primejailbait.com/gallery_inf.php?page={}&cat=1&order=DESC&lastseen={}'.format(sc.page, sc.last)
scrap()



# req = requests.get('https://teengallery.com/index.php')
# soup = bs4.BeautifulSoup(req.text, 'html.parser')
#
# for link in soup.select('.sidethumb'):
#     selector = link.get('style')
#     id = selector.rsplit('/', 1)[-1].replace('\');', '')
#     print('https://teengallery.com/resized/' + id, './photos/' + id)
#     urllib.request.urlretrieve('https://teengallery.com/resized/' + id,  id)

import requests
import bs4
url = 'https://www.apple.com/itunes/charts/songs/'
respone = requests.get(url)
songs = bs4.BeautifulSoup(respone.content,'html.parser')
div = songs.find('div', id = 'main')
all_li_tag = div.find_all('li')
data_crawled = []
for li in all_li_tag:
    print(li.h3.a)
    print(li.h4.a)


import requests
import urllib.request
from bs4 import BeautifulSoup
import csv
import datetime
import time
#from oauth2client.service_account import ServiceAccountCredentials
from bs4 import CData

datetime.datetime.today()
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')


def 멜론():
    if __name__ == "__main__":
        RANK = 100
    
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        req = requests.get('https://www.melon.com/chart/day/index.htm', headers = header)
        html = req.text
        parse = BeautifulSoup(html, 'html.parser')
    
        titles = parse.find_all("div", {"class": "ellipsis rank01"}) 
        singers = parse.find_all("div", {"class": "ellipsis rank02"}) 
        albums = parse.find_all("div",{"class": "ellipsis rank03"})
    
        title = []
        singer = []
        album = []
        tnumber= []
        snumber= []

        for t in titles:
            title.append(t.find('a').text)
    
        for s in singers:
            singer.append(s.find('span', {"class": "checkEllipsis"}).text)

        for n in titles:
            tnumber.append(n.find('a'))

        for s in singers:
            snumber.append(s.find('span', {"class": "checkEllipsis"}))

        # with open('new_melon.csv', 'a', encoding='utf-8-sig', newline='') as f:
        #     melonwriter=csv.writer(f)
        #     melonwriter.writerow([nowDatetime])
        #     melonwriter.writerows([title,singer,tnumber,snumber])
        #     f.close()
        a = list(zip(title, singer))
        for b in a:
            print(", ".join(b))
        # print(title, singer)

멜론()
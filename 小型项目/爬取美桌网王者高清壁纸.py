import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import threading
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
img_list = []
URLS = []
def pick_gqbz():
    for l in range(1,6):
        urls = "http://www.win4000.com/mt/wangzherongyao_" + str(l) + str(".html")
        response = requests.get(urls, headers = headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        img_list = soup.find_all("ul", attrs={"class":"clearfix"})
        temp = str(img_list).split()
        for i in range(len(temp)):
            if len(temp[i]) < 35:
                #print(len(temp[i]))
                continue
            if temp[i][6:34] == 'http://www.win4000.com/meinv':
                #print(temp[i])
                URLS.append(temp[i][6:-1])
            else:
                continue
    for k in range(len(URLS)):
        response = requests.get(URLS[k], headers = headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        img_list = soup.find_all("img", attrs={"class":"pic-large"})
        a, b = str(img_list).rfind('http', 1), str(img_list).rfind('jpg', 1)
        img_url = str(img_list)[a:int(b) + 3]
        filename = img_url.split("/")[-1]
        fullpath = os.path.join("images", filename)
        while img_url[-4:] == ".gif":
            continue
        request.urlretrieve(img_url, fullpath)
        print("%s下载完成" % filename)
if __name__ == "__main__":
    pick_gqbz()

import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import threading
PAGE_URLS = []
IMG_URLS = []
gLock = threading.Lock()
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
def producer():
    while True:
        gLock.acquire()
        if len(PAGE_URLS) == 0:
            gLock.release()
            break
        page_url = PAGE_URLS.pop()
        gLock.release()
        response = requests.get(page_url, headers = headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        img_list = soup.find_all("img", attrs={"class":"img-responsive lazy image_dta"})
        for img in img_list:
            img_url = img['data-original']
            IMG_URLS.append(img_url)
def consumer():
    while True:
        gLock.acquire()
        if len(IMG_URLS) == 0 and len(PAGE_URLS) == 0:
            gLock.release()
            break
        if len(IMG_URLS) > 0:
            img_url = IMG_URLS.pop()
        else:
            img_url = ''
        gLock.release()
        if img_url:
            filename = img_url.split("/")[-1]
            fullpath = os.path.join("images",filename)
            request.urlretrieve(img_url, fullpath)
            print("%s下载完成" % filename)
def main():
    for i in range(1, 100):
        page_url = "https://www.doutula.com/photo/list/?page=" + str(i)
        PAGE_URLS.append(page_url)
    #5个生产者线程
    for j in range(10):
        th = threading.Thread(target=producer)
        th.start()
    #5个消费者线程
    for k in range(10):
        th = threading.Thread(target=consumer)
        th.start()
if __name__ == "__main__":
    main()import requests
from bs4 import BeautifulSoup
from urllib import request
import os
import threading
PAGE_URLS = []
IMG_URLS = []
gLock = threading.Lock()
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
def producer():
    while True:
        gLock.acquire()
        if len(PAGE_URLS) == 0:
            gLock.release()
            break
        page_url = PAGE_URLS.pop()
        gLock.release()
        response = requests.get(page_url, headers = headers)
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        img_list = soup.find_all("img", attrs={"class":"img-responsive lazy image_dta"})
        for img in img_list:
            img_url = img['data-original']
            IMG_URLS.append(img_url)
def consumer():
    while True:
        gLock.acquire()
        if len(IMG_URLS) == 0 and len(PAGE_URLS) == 0:
            gLock.release()
            break
        if len(IMG_URLS) > 0:
            img_url = IMG_URLS.pop()
        else:
            img_url = ''
        gLock.release()
        if img_url:
            filename = img_url.split("/")[-1]
            fullpath = os.path.join("images",filename)
            request.urlretrieve(img_url, fullpath)
            print("%s下载完成" % filename)
def main():
    for i in range(1, 100):
        page_url = "https://www.doutula.com/photo/list/?page=" + str(i)
        PAGE_URLS.append(page_url)
    #5个生产者线程
    for j in range(10):
        th = threading.Thread(target=producer)
        th.start()
    #5个消费者线程
    for k in range(10):
        th = threading.Thread(target=consumer)
        th.start()
if __name__ == "__main__":
    main()

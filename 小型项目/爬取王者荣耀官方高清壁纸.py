#官方所有英雄皮肤（91个）
#代码内容注释详细，一起学习。

import requests
#import os
url = "https://pvp.qq.com/web201605/js/herolist.json"   #想要爬取的网址

'''
请求头：User-Agent:简称UA，它是一个特殊的字符串头,可以使服务器识别客户使用的操作系统及版本
在做爬虫时加上此信息,可以伪装成浏览器,如果不加很可能会被识别出为爬虫,这个一般从Chrome的开发者
工具中可以得到,在Network里面的Headers(也就是请求头)
'''

header = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
response = requests.get(url, headers=header)    #常见的请求方法：get
hero_list = response.json()     #解析方式
hero_name = list(map(lambda x:x["cname"], hero_list))   #使用map()函数和lambda()函数

#map()会根据提供的函数对指定序列进行映射,第一个参数是函数,第二个参数是序列对象
#lambda()函数可以作为map的提供函数,它本身叫匿名函数

hero_number = list(map(lambda x:x["ename"], hero_list))

def save_IMG():
    num = 0
    for i in hero_number:
        for j in range(10):
            img_url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + str(i) + "/" + str(i) + "-bigskin-" + str(j) + ".jpg"
            hl = requests.get(img_url)
            if hl.status_code == 200:   #这里是响应状态码,当status_code为200时,表明服务器已成功处理了请求.
                with open(r"/home/honorwh/tmp/" + hero_name[num] + str(j) + '.jpg', 'wb') as f:     #这里用with关键字和正则把存储路径精确表示.
                    f.write(hl.content)     #requests库的方法
        num += 1
save_IMG()

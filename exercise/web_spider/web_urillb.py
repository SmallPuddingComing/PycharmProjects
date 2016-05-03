#coding:utf8

import requests
import re
import gevent
from multiprocessing import Process
from gevent.pool import Pool

data = {'name'}
header = {'content-type':'application/json'}
urls = 'http://www.zhihu.com/topic/19554091/questions?page=1'
zhihu_url = 'http://www.zhihu.com/'

r = requests.get(urls)
html = r.content

m1 = re.findall('.yy.[0-9]{5}', '#yy-12433')
print m1


qurl = r'question/[__0-9__]{8}'
qurlist =re.findall(qurl, html)
for each in qurlist:
    url = zhihu_url + str(each)
    r1 = requests.get(url)
    print r1.text



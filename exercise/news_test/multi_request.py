#coding:utf8
from gevent import monkey
monkey.patch_all()
import urllib2
from gevent.pool import Pool

'''并发出100个web请求
'''
def download(url):
    response = urllib2.urlopen(url, timeout=100)
    if response.getcode() == 200:
        return urllib2.urlopen(url, timeout=100).read()

if __name__ == '__main__':
    urls = ['http://httpbin.org/get'] * 10
    pool = Pool(20)
    print pool.map(download, urls)
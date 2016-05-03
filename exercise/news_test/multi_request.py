#coding:utf8
import profile
import urllib2, os
import gevent
from gevent import monkey
monkey.patch_all()
import multiprocessing
from multiprocessing.process import Process
from multiprocessing.pool import Pool


'''并发出100个web请求'''
def download(url):
    try:
        response = urllib2.urlopen(url, timeout=100)
        if response.getcode() == 200:
            text = urllib2.urlopen(url, timeout=100).read()
            print 'ok '
    except Exception as e:
        print("can not connect to url ,{0}".format(str(e)))

def multi_gevent(urls):
    for url in urls:
        down_obj = gevent.spawn(download, url)
        gevent.joinall([down_obj])

if __name__ == '__main__':
    urls = ['http://httpbin.org/get'] * 10

    # p = os.fork()#开启一个子进程

    #process,开启了50个greenlet，协程完成就还退出loop
    processList = []
    for i in xrange(5):
        process = Process(target=multi_gevent, args=(urls,))
        processList.append(process)
        process.start()

    for pro in processList:
        pro.join()

    #process pool这是map内部封装了开启线程运行
    # print multiprocessing.cpu_count()
    # pool = Pool(multiprocessing.cpu_count())
    # pool.map(download, urls)
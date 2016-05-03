#coding:utf8
'''
Created on 2016-4-1

@author : yr
website from : http://www.jb51.net/article/80115.htm
'''
import multiprocessing
import requests
from multiprocessing.process import Process

#IO密集型任务
#多个进程同时下载多个网页
#利用Queue+多进程
#由于是IO密集型，所以同样可以用threading

'''
1、初始化tasks，里面放着一系列的dest_url
2、同时开启4个进程向tasks中获取任务进行执行
3、处理结果贮存在一个result
'''

def main():
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    cpu_count = multiprocessing.cpu_count()#进程数==CPU核数目

    create_process(tasks, results, cpu_count)
    add_tasks(tasks)
    parse(tasks, results)

def create_process(tasks, results, cpu_count):
    for _ in range(cpu_count):
        p = multiprocessing.Process(target=_worker, args=(tasks, results))
        p.daemon = True #子进程随主进程的关闭而关闭
        p.start()

def _download(task):
    '''下载网页
    '''
    try:
        request = requests.get(task)
        if request.status_code == 200:
            return request.text
    except Exception as e:
        print ("connect the url is fail ,{0}".format(str(e)))

def _worker(tasks, results):
    while True:
        try:
            task = tasks.get()
            result = _download(task)
            results.put(result)
        finally:
            tasks.task_done()

def get_urls():
    urls = ["http://httpbin.org/get"] * 10
    return urls

def add_tasks(tasks):
    for url in get_urls():
        tasks.put(url)

def _parse(results):
    print results

def parse(tasks, results):
    try:
        tasks.join()
    except KeyboardInterrupt as e:
        print ("tasks has been stopped ,{0}".format(str(e)))

    while not results.empty():
        _parse(results)

if __name__ == '__main__':
    main()




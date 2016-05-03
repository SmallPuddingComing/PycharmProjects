#coding:utf8

from redis import Redis
'''
网络I/O是单线程复用I/O
不支持数据一致性，但是可以支持原子操作，支持事务
内存管理方面会有一些内存碎块，非暂时性的数据不能被剔除
存贮方式是key-value、set、sorted、hash
总结：
1.Redis使用最佳方式是全部数据in-memory。
　　2.Redis更多场景是作为Memcached的替代者来使用。
　　3.当需要除key/value之外的更多数据类型支持时，使用Redis更合适。
　　4.当存储的数据不能被剔除时，使用Redis更合适
'''
class RedisQueue(object):
    def __init__(self, name, namespace='queue', **redis_kwargs):
        self.__db = Redis(**redis_kwargs)
        self.key = "%s :%s" % (namespace, name)

    def qsize(self):
        return self.__db.llen(self.key)

    def empty(self):
        return self.qsize() == 0

    def put(self, item):
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self.key, timeout) #if empty, blocking
        else:
            item = self.__db.lpop(self.key)  #if empty,return nothing

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        return self.get(False)

    def clear(self):
        for i in xrange(self.qsize()):
            item = self.get()
            self.__db.delete(item)

        if self.empty():
            print "queue is empty"

if __name__ == '__main__':
    q = RedisQueue('test')
    q.put('mingtian')
    q.put('hello, world!')
    q.put('ni hao')
    if q.qsize():
        print q.get()

    print q.qsize()
    if not q.empty():
        q.clear()

    # print q.get_nowait()






#coding:utf-8

'''
define the __call__ function can direct play the object instance
'''

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'user':
            return Chain('%s %s' % (self._path, path))   #it is exchange the old path
        else:
            return Chain('%s' % self._path)

    def __str__(self):
        return 'My Path is: %s' % self._path
    __repr__ = __str__

    def __call__(self, name):
        return Chain('(Get User name is: %s) ' %  name)


if __name__ == '__main__':
    c = Chain('3234')
    print c('hello')
    print Chain('123').user('hehe').us         #init - getatter - init - call - init - getatter - init - str
    print Chain().user('mimi').user
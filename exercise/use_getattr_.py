#coding:utf-8

'''
dong tai add the attribute --- getattr
'''

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 98
        raise AttributeError('\'student \' object has no attribute \'%s \'' % attr)


if __name__ == '__main__':
    s = Student()
    print s.score
    print s.abc


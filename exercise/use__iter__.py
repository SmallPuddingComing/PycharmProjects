# coding:utf-8

'''
this inbuilt function is use for diedai and xunhuan ,return the result is deidai object
'''

class Fibnaci(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        self.a , self.b = self.b , self.a + self.b
        if self.a > 100:    # exit the xunhuan conditional
            raise StopIteration
        return self.a

    def __str__(self):
        return 'result is :%s %s' % (self.a , self.b)

if __name__ == '__main__':
    fb = Fibnaci()
    print fb

    i=0
    for fb1 in Fibnaci() :
        i+=1
        if i <= 5:
            print fb1
        else:
            break

    #print Fibnaci()[5]   #it can not use like list,just for forxunhuan



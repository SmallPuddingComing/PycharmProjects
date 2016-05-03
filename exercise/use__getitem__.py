# coding:utf-8

'''
use getitem like iter to try complete a fiboniac function
'''

class Fibonac(object):          #this is fixup by me
    def __getitem__(self, n):
        if isinstance(n, int):
           return self.calc(n, 1)

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            #a, b = 1, 1
            L = []
            a , b= self.calc(start, 0)
            for x in range(start ,stop):
                L.append(a)
                a, b = b, a+b
            return L

    def calc(self, n, args):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        if args == 1:
            return a
        else:
            return a, b


    def __str__(self):
        return 'mabey this is error'


class Fab(object):           #this  is example from liaoxuefeng website
    def __getitem__(self, n):
        a , b = 1, 1
        if isinstance(n , int):
            if n < 0:
                start = n
                end = 0
            else:
                start = 0
                end = n
            for x in range(start, end):
                a , b = b, a+b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step

            if step == None:
                step = 1

            L = []
            for x in range(0,stop,step):
                if x >= start:
                    L.append(a)
                a , b = b , a+b
            return L


class Fibo(object):      #this is use dict to complete the fibonaic
    def __init__(self):
        self.Dd = {}
        self.__setitem__(0,1)
        self.__setitem__(1,1)

    def __getitem__(self, mystr):
        if isinstance(mystr, str):
            key = mystr
            return self.Dd[key]

        if isinstance(mystr, int):
            for x in range(mystr):
                self.Dd[x+2]  = self.Dd[x] + self.Dd[x+1]
            return self.Dd[x]


    def __setitem__(self, key, value):
        self.Dd[key] = value

    def __delitem__(self, key):
        del self.Dd[key]




if __name__ == '__main__':
    f= Fibonac()
    print f[1:12]
    print f[5]

    f1 = Fab()
    print f1[-4]
    print f1[4:12:2]

    f2 = Fibo()
    print f2[4]

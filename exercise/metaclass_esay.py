#coding = utf-8

'''
this is example for metaclass
'''

class Metaclass(type):
    def __new__(cls, name, base, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, base, attrs)


class MyList(list):
    __metaclass__ = Metaclass

if __name__ == '__main__':
    L = MyList()
    L.add('1')
    print L
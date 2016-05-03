# -*- coding = utf-8 -*-

''' use _slots_ to add the attrubition for class
'''

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student name is %s' % self.name
    __repr__ = __str__

if __name__ == "__main__":
    s = Student('Michal')
    print s
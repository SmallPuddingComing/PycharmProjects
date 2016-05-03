#coding = utf-8

'''
this is python metaclass
'''

class MyShinyClass(object):
    pass

class Foo(object):
    bar = True
    name = 'lili'

class FooChild(object):
    user = '12345'
    paswerd = '123456'



if __name__ == '__main__':
    MyShinyClass = type('MyShinyClass', (), {})
    print MyShinyClass            #create the object for class ,the class name as for one Usages
    print MyShinyClass()          #create the instance for class
    print type(MyShinyClass)      #the type is class
    print type(MyShinyClass())    #create the instance for class

    print '-' * 40

    Foo = type('Foo', (), {'bar' : False, 'name' : 'henan'})
    print Foo.bar, Foo.name

    def eroch_bar(self):        #add the function for class
        print 'user is %s, passwerd is %s' % (self.user, self.paswerd)

    FooChild = type('FooChild', (Foo,) , {'user' : 'www', 'paswerd' : '123456', 'eroch_bar' : eroch_bar})  #inherit the Foo class use the type
    print hasattr(Foo, 'eroch_bar')
    print hasattr(FooChild, 'eroch_bar')
    my_foo = FooChild()
    print my_foo.eroch_bar()

    print '-' * 40

    f = FooChild()
    print f.user, f.paswerd



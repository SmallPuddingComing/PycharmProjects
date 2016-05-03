#coding = utf-8

'''
this is myself define metaclass for example
'''

def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''
    return a class object ,with the list of its attribute turned into uppercase
    '''

    #pick up any attribute that don't start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    #let 'type' do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)

    #this will affect all classes in the module
__metaclass__ = upper_attr





class Foo():
    bar  = 'xiao'

print hasattr(Foo, 'bar')
print hasattr(Foo, 'Bar')

foo = Foo()

print foo.BAR                        # why can't to acheive the Bar

Foo = upper_attr('Foo', (), {'bar' : 'xiao'})
print Foo.BAR



class UpperAttrMetaclass(type):        #inherit the type class ,you can define again the __new__() function
    def __new__(cls, name, base, dict):
        upper_attr = {}
        for name1, val in dict.items():
            if not name1.startswith('__'):
                upper_attr[name1.upper()] = val
            else:
                upper_attr[name1] = val

        return type.__new__(cls,name,base,upper_attr)

class Noo():
    name = 'ming'

Noo = UpperAttrMetaclass('Noo', (), {'name' : 'ming'})     #constructed function is diaplay the new function
print Noo.NAME

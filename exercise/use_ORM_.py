#coding = utf-8

'''
Object Relational Mapping ,one class linked the one table reflect in sql
'''

class Filed(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)

class StringFiled(Filed):
    def __init__(self, name):
        super(StringFiled, self).__init__(name, 'varchar(100)')

class IntegerFiled(Filed):
    def __init__(self, name):
        super(IntegerFiled, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, base, attrs):
        if name == 'Model':
            return type.__new__(cls, name, base, attrs)
        mappings = dict()
        for key ,val in attrs.iteritems():
            if isinstance(val, Filed):
                print 'mapping has key-value %s %s' % (key, val)
            mappings[key] = val
        for key in mappings.iterkeys():
            attrs.pop(key)

        attrs['__table__'] = name          #class name is table name
        attrs['__mappings__'] = mappings   #atrribute in mappings reflect in col

        return type.__new__(cls, name, base, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model'object has no atrribute: '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fileds = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fileds.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s)  value (%s) ' % (self.__table__, ','.join(self.fileds), ','.join(self.params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(self.args))


    def update(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass

class User(Model):
    #define atrribute of class by col
    id = IntegerFiled('id')
    name = StringFiled('username')
    email = StringFiled('email')
    passwred = StringFiled('paswerd')



u = User(id =123, name = 'Michael', email = 'test@orm.com', passwred = 'mypaswed')
u.save()
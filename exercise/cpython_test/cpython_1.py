#coding:utf8

from ctypes import *
from platform import *

cdll_names = {
    'Darwin' : 'libc.dylib',
    'Linux' : 'libc.so.6',
    'Windows' : 'msvcrt.dll'
}

#数据隐式转换
clib = cdll.LoadLibrary(cdll_names[system()])
s3 = clib.strcat('a', 'b')#没有确定类型
print s3
clib.strcat.restype =c_char_p
s4 = clib.strcat('c', 'b')
print s4

#数据回流
s1 = c_char_p('hello')
s2 = clib.strcat(s1, 'b')
print s1.value

#输出格式
clib = cdll.LoadLibrary(cdll_names[system()])
clib.printf(c_char_p("Hello %d %f"), c_int(15), c_double(2.3))
#输出格式的拆解
format_str = c_char_p()
int_val = c_int()
double_val = c_double()

format_str.value = "Hello %d %f"
int_val.value = 15
double_val.value = 2.3
print clib.printf(format_str, int_val, double_val)

#高级类型映射--数组
#在c语言中，char是一种数据类型，而char[100[又是另外一种数据类型，
#因此在ctypes中，创建数组需要预先生成需要的数组类型、

#这个需要是在visual2008下面进行原源代码的实现。

#--简单类型指针
type_p_int = POINTER(c_int)#创建一个指针类型
v = c_int(4)
p_int = type_p_int(v)
print '-'*40
print p_int[0]
print p_int.contents
print '#' + '-'*40 + '#'

p_int = pointer(v)
print type(p_int[0])
print p_int[0]
print p_int.contents

#函数指针
print '#' + '-'*40 + '#'
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))

def py_cmp_func(a, b):
    print type(a)
    print "py_cmp_func", a[0], b[0]
    return a[0] - b[0]

type_array_5 = c_int * 5
ia = type_array_5(5, 1, 7, 33, 99)
clib.qsort(ia, len(ia), sizeof(c_int), CMPFUNC(py_cmp_func))


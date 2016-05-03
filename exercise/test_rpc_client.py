#coding:utf8
import pstats #用Cprofile输出邮件的性能分析二进制流，进行二次分析。
import cProfile
import xmlrpclib
#继承与同步调用的TCP 和XML-rpc request
def client():
    proxy = xmlrpclib.ServerProxy("http://127.0.0.1:8080")
    print proxy.add(3,7)
    print proxy.subtract(7, 3)
    try:
        print proxy.multiply(7, 3)
    except Exception as e:
        print "have no function %s" % 'multiply'


# multicall = xmlrpclib.MultiCall(proxy)
# multicall.add(3, 7)
# multicall.subtract(7, 3)
# multicall.multiply(7, 3)
# multicall.divide(7, 3)
# result = multicall()

# print "7+3=%d, 7-3=%d, 7*3=%d, 7/3=%d" % tuple(result)

if __name__ == '__main__':
    cProfile.run('client()')
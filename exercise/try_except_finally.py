#coding = utf-8

'''
deal with the error use the try-except-finally
'''

import logging
logging.basicConfig(level=logging.INFO)

def foo(num):
    #assert num != 0, 'num is zore!'    # 1-use assert function
    logging.info("num = %d" % num)      # 2-use logging (Model:debug/infor/warring/error)
    return 10 / num                    # 3-use the duandian

def bar(num):
    return foo(num) * 2

def Tool(num):
    try:
        return bar(num)
    except:
        ValueError ("the number is error %s" % num)
    finally:
        print 'finally'

    print 'END'

print foo(0)
if __name__ == '__main__':
    while True:
        num_1 = raw_input("Enter a Integer Number:")
        print Tool(int(num_1))
        if num_1 == 's':
            exit()
#coding:utf8

import socket, sys

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', 51422))
        print "i am client 2"
    except socket.error, e:
        print "connect error %s" % str(e)
        sys.exit(0)

    while True:
        try:
            buf = s.recv(2048)
            if "dose not exist" in buf:
                print "filename is not exist"
                sys.exit(0)
            else:
                if not len(buf):
                    break

            sys.stdout.write(buf)#在控制台下打印出buf

            try:
                s.sendall(raw_input() + '\r\n')#换行符
            except socket.error, e:
                print "send data erro %s" % str(e)

        except socket.error, e:
            print "recv error %s" % str(e)
            sys.exit(0)



if __name__ == '__main__':
    client()

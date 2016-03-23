#coding:utf8

import socket, sys


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 51422))
    s.listen(1)
    while True:
        clientsocket, clientaddr = s.accept()
        clientfile = clientsocket.makefile('rw', 0)
        clientfile.write("welcome" + str(clientaddr) + '\n')
        clientfile.write("Please enter a string:")
        line = clientfile.readline().strip()#取出字符串头尾的空格（TAB 和 换行）
        clientfile.write("You entered %d characters" % len(line))
        clientfile.close()
        clientsocket.close()

if __name__ == '__main__':
    server()

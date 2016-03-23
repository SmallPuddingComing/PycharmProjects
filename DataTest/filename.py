# -*- coding = utf-8 -*-


#Foundations of Python Network Pragramming

#import socket
#hostname = 'google.com'
#addr = socket.gethostbyname(hostname)
#print 'The address of', hostname, 'is' , addr

import socket
import sys

MAX  = 65535
PORT = 1060

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if sys.argv[1:] == ['server']:
    s.bind(('127.0.0.1', PORT))
    print 'Listening at', s.getsockname()

    while True:
        data, address = s.recvfrom(MAX)
        print 'The client at ', address , 'says' , repr(data)
        s.sendto('Your data was %d bytes' % len(data) , address)

elif sys.argv[1:] == ['client']:
    s.bind(('127.0.0.1', 1061))
    print 'Address before sending:', s.getsockname()

    s.sendto('This is my message', ('127.0.0.1', PORT))
    print 'Adderss after sending',  s.getsockname()

    data ,address = s.recvfrom(MAX)
    print 'The server', address, 'says', repr(data)

else:
    print >>sys.stderr, 'usage: udp_local.py sever|client'

#coding:utf8

import gevent
from gevent import monkey
monkey.patch_all()

#聊天服务器
from gevent.queue import Queue
from  gevent.server import StreamServer#是一个通用的TCP服务器

users = {}     #user dict save queue
sock_dict = {} #collect sock dict
def broadcast(username, msg, toName=None):
    msg += '\n'
    if users.get(username, None):
        # if toName:
        users[username].put([msg, toName])
        # else:
        #     users[username].put([msg, ])

    # for v in users.values():
    #     v.put(msg)

def reader(username, f):
    toName = None
    for l in f:
        if l == '\r\n':
            message = l.strip()
        else:
            toName, message = l.strip().split(':')
        msg = '%s> %s' % (username, message)#(username, l.strip())
        broadcast(username, msg, toName)

def findSockByName(name):
    for key ,val in sock_dict.iteritems():
        nameLists = val
        for namelist in nameLists:
            if namelist[0] == name:
                return key
    else:
        return None

def isMyChatFriend(nameLists, toName):
    friend = []
    for namelist in nameLists:
        fName = namelist[1]
        friend.append(fName)
    if toName in friend and toName:
        return True
    return False

def writer(q, sock):#q, sock
    while True:
        nameLists = sock_dict[sock]
        n = nameLists[0][0]
        msg, toName = users.get(n, None).get()
        if isMyChatFriend(nameLists, toName):
            s = findSockByName(toName)
            if s:
                s.sendall('From '+msg)
            else:
                sock.sendall('you friend not online')
            # gevent.sleep(1)
        else:
            sock.sendall('wait\n')
            # gevent.sleep(1)

def read_name(f, sock):
    while True:
        sock.sendall('Please enter you name:')
        name = f.readline().strip()
        sock.sendall('Please enter you want chat name:')
        fName = f.readline().strip()
        if name:
            if name in users:
                sock.sendall('That username is alreadly taken.\n')
            else:
                sock.sendall('welcome !\n')
                return name, fName

def handle(sock, client_addr):
    f = sock.makefile('rb', 0)
    name, fName= read_name(f, sock)

    #save the sock
    if sock_dict.get(sock, None):
        namelist = sock_dict[sock]
        if namelist:
            for v in namelist:
                if fName not in v:
                    continue
                else:
                    break
            else:
                sock_dict[sock].append([name, fName])
    else:
        sock_dict[sock] = []
        sock_dict[sock].append([name, fName])
    print "print sock_dict",sock_dict

    broadcast(name, ('## %s joined from %s' % (name, client_addr[0])))
    print '## %s joined from %s' % (name, client_addr[0])

    #create a queue for save the client message
    q = Queue()
    users[name] = q

    try:
        r = gevent.spawn(reader, name, f)
        w = gevent.spawn(writer, q, sock)
        gevent.joinall([r, w])

    finally:
        del(users[name])
        broadcast(name, '## %s left is chat')

def handle_1(sock, addr):
    sock.send("Hello from a telent! \n")
    for i in range(5):
        sock.send(str(i) + '\n')
    sock.close()

if __name__ == '__main__':
    import sys
    try:
        myip = sys.argv[1]
    except IndexError:
        myip = '0.0.0.0'

    print 'To join , telnet %s 51422' % myip
    s = StreamServer((myip, 51422), handle)
    s.serve_forever()
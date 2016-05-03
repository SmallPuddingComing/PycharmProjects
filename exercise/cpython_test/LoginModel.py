#coding:utf8

import urllib2
import urllib
import re
import random
import twisted

''' python model use in c++ program'''
def Login(uid, passwrd):
    params = urllib.urlencode({'id':uid, 'pw':passwrd})
    headers = {'Referer':'http://bbs.nju.edu.cn/cache_bbsleft.htm'}

    #uidir是随机生成每个用户的线程，如‘/vd89905’
    uidir = '/vd' + str(random.randint(100, 100000))

    url = 'http://bbs.nju.edu.cn/cache_bbsleft.htm'
    data = {'id':uid, 'pw':passwrd}
    response = urllib2.urlopen(url, data, timeout=20)

    msg = response.read()
    if response.getcode() == 200:
        print ">>>> login success!"

    patt = '\'(\d+)N' + uid +  '\'(\d+)\''
    cookieOrigin = re.findall(patt)
    cookies = []
    #小百合设置对_U_NUM+2，对_U_KEY-2
    cookies.append(str(int(cookieOrigin[0][0])+2))
    cookies.append(str(int(cookieOrigin[0][1])-2))
    cookie = '_U_NUM='+cookies[0]+'; _U_UID='+ uid + '_U_KEY='+cookies[1] + 'FOOTKEY=;'

    return cookie



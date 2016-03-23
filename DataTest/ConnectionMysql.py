# -*- coding:utf8 -*-

_framework_ = 'firefly v1.2.3'
_author_ = '尔荳荳'
_date_ = "Sdate:2015/7/31"
_license_ = "python"

from gfirefly.server.globalobject import netserviceHandle
from gfirefly.server.globalobject import GlobalObject
from datetime import *
from gfirefly.dbentrust.dbpool import dbpool

import json ,sys,os,time, hashlib

class ConnectionMysql:
    '''the class use for connect with the datebase '''
    def _init_(self):
        self.dbConfig = json.load(open('config.json', \
                'r')).get('db')
        dbpool.initPool(host = self.dbConfig['host'], \
                    user = self.dbConfig['user'], \
                    passwd = self.dbConfig['passwd'], \
                    port = self.dbConfig['port'], \
                    db = self.dbConfig['db'], \
                    char = self.dbConfig['charset'])
        self.conn = dbpool.connection()
        self.cursor = self.conn.cursor()

    def getOne(self, sqlStr):
        ''' get a sclie date'''
        try:
            self.cursor.execute(sqlStr)
            result =  self.cursor.fetchone()
            return result
        except Exception,e:
            print '[ERROR]:',e
            return False

    def getList(self,sqlStr):
        '''get a lots of datas'''
        try:
            self.cursor.execute(sqlStr)
            result = self.cursor.fetchall()
            return result
        except Exception,e:
            print '[EORRO]:',e
            return  False

    def query(self, sqlStr):
        '''
         deal with some opeateration such as insert/delete/upate
        '''
        if 'insert into' not in sqlStr.lower() and 'update' not in sqlStr.lower() and 'delete from' not in sqlStr.lower():
            return  False
        try:
            self.cursor.execute(sqlStr)
        except Exception,e:
            print '[EORRO]',e
            return False

        if 'insert' in sqlStr.lower():
            self.cursor.execute("SELECT @@IDENITIY AS id")
            result = self.cursor.fetchone()
            return result[0]
        return True

    def close(self):
        '''  close the datebase'''
        self.cursor.close()
        self.conn.close()
        self.conn = False

dbObject = ConnectionMysql()
authenticationKey = '32921hhjijk1j292h21ll1k20'        #定义用户验证随机率
loginTempList = []                                         #define the list save the inforn  from user login






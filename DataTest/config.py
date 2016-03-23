#-*- coding = utf-8 -*-
#name:config.py

import ConfigParser
#import os

def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    #path = os.path.split(os.path.realpath(file))[0] + '/db.conf'
    config.read("db.conf")
    #print config.get("dbname","dbpassword")
    return config.get(section, key)




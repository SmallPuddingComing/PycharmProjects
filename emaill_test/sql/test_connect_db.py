#coding:utf8

import MySQLdb

#连接数据库
conn = MySQLdb.connect(host='127.0.0.1', port=3306,  user='root', passwd='123456', db='test', charset='utf8')#'localhost'会导致连接不上服务器
#建立游标
cursor = conn.cursor()
#cursor = MySQLdb.SSCursor(conn) , use_unicode=True
count = 0
try:
    #创建user表
    cursor.execute("create table player (id varchar(20) primary key, name varchar(20))")
    #随便插入一行数据，方便后续查询
    sql = "insert into player (id,name) values (%s,\"%s\")" % ('4',"he")
    cursor.execute(sql)
    count = cursor._do_query() #打印行的数量

except MySQLdb.Error, e:
    print "MySQL Error %d: %s" % (e.args[0], e.args[1])

    try:
        # sql = "insert into player (id,name) values (%s,\"%s\")" % ('11',"fff")
        cursor.execute("insert into player (`id`,`name`) values (%s,%s)", ('13',"jjj"))
        print cursor.rowcount #打印行的数量
    except MySQLdb.Error, e:
        print "MySQL Error %d: %s" % (e.args[0], e.args[1])

finally:
    #提交事务
    conn.commit()
    cursor.close()


#运行查询
cursor = conn.cursor()
# sql = 'select * from player where id >= %s' % '1'
cursor.execute('select * from player where id=%s', '1')
values = cursor.fetchall()
print values
print cursor.rowcount
cursor.close()
conn.close()
#coding:utf8
mystr = "对不起！"
number = ['0','1','2','3','4','5','6','7','8','9','10']
c_number = ['零','一','二','三','四','五','六','七','八','九','十']
mydict = dict(zip(number, c_number))
z_dict = {'10000':'万','1000':'千','100':'百','10':'十','1':''}

def changeNumber(num):
    num = str(num)
    mynum = ""
    for i, val in enumerate(num):
        if mydict[val]:
            if mydict[val] == '零':
                #这个情况是保证有夹心0，比如1010，1001,1100
                if num[i]== '0':
                    if i >= len(num)-1:
                        continue
                    if num[i+1]=='0':
                        continue
            #汇总结果
            mynum += mydict[val]
        else:
            mynum = mydict[val]

        #这里是加上单位，例如'万'
        n = len(num)-int(i)-1
        if z_dict[str(10**n)] and mydict[val]!='零':
            mynum += z_dict[str(10**n)]
        else:
            continue

    return mynum

def playMsgTimes(num, mystr):
    i_sum = 0
    for i in xrange(num):
        i_sum += 1
        print mystr + " " + '第' + changeNumber(i_sum) + '遍'

if __name__ == '__main__':
    playMsgTimes(12000, mystr)

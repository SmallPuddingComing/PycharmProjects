# -*- coding = utf-8 -*-

"this is programm used for multiples 3 and 5"

a, b = 3, 5
maxNum = 1000
def Mulitples(n):
    if n % a==0 or  n % b==0:
        return True
    else:
        return False


count = 0
for i in range(maxNum):
    if Mulitples(i) is not False:
        count += 1


print  count
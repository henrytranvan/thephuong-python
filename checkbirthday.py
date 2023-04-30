import datetime 
import os

now = datetime.datetime.now()
checkdaymonth = now.strftime("%m/%d")
d = checkdaymonth.split()
f = open("a.txt",'r',encoding = 'utf-8')
while True :
    a = f.readline()
    if a == "" :
        break
    b = a.split()
    c = b[-1:]
    if c == d :
        print("Hôm nay là ngày sinh nhật của : " + str(a))
        os.system("pause")
    



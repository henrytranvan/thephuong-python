import datetime 

now = datetime.datetime.now()
checkdaymonth = now.strftime("%m/%d")

print(checkdaymonth)
f = open("a.txt",'r',encoding = 'utf-8')
while True :
    a = f.readline()
    print(a)
    if a == "" :
        break
    b = a[-1:4]
    while True :    
        print(b)
        if True :
            break  


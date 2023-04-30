import datetime 

now = datetime.datetime.now()
checkday = now.strftime("%d")
checkmonth = now.strftime("%m")
if checkday == "30" :
    print("true")
else :
    print("false")
if checkmonth == "04" :
    print("True")
else :
    print(False)

print(checkday)
print(checkmonth)
f = open("kct.txt",'r',encoding = 'utf-8')
while True :
    a = f.readline() 
    print(a)
    if a == "" :
        break
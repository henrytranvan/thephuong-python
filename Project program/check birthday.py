import datetime 

now = datetime.datetime.now()
checkday = now.strftime("%d")
checkmonth = now.strftime("%m")
if checkday == "30" :
    print("true")
else :
    print("false")
if checkmonth == "4" :
    print(True)
else :
    print(False)


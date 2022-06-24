s = input("Nhập câu của bạn: ") 
d={"UPPER CASE": 0, "LOWER CASE" : 0}
for i in s:
    if i.isupper(): 
        d["UPPER CASE"]+=1
    elif i.islower(): 
        d["LOWER CASE"]+=1
    else:
        pass
print ("Chữ hoa:", d["UPPER CASE"]) 
print ("Chữ thường:", d["LOWER CASE"])

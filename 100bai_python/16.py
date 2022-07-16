s = input("Nhập câu của bạn: ") 
# Bài tập Python 16, Code by Quantrimang.com 
d={"sotu":0, "socau":0}
for c in s: 
    if c.isdigit(): 
        d["sotu"]+=1 
    elif c.isalpha(): 
        d["socau"]+=1 
    else: 
        pass 

print ("Số chữ cái là:", d["sotu"]) 
print ("Số chữ số là:", d["socau"])
def NumGenerator(n): 
    for i in range(n+1): 
        if i%5==0 and i%7==0: 
            yield i 
            
n=int(input("Nhập n: ")) 
values = [] 
for i in NumGenerator(n): 
    values.append(str(i)) 
    print ("Các số chia hết cho 5 và 7 trong khoảng 0 và n là: ",",".join(values))
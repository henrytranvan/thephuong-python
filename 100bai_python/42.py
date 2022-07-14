tp=(1,2,3,4,5,6,7,8,9,10) 
ds=list() 
for i in tp: 
    if tp[-i]%2==0: 
        ds.append(tp[i]) 
tp2=tuple(ds) 
print (tp2)
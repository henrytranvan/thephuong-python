print('Nhap 1 mang cac so')
ketthuc = False
ds = []
while (ketthuc != True) :
    a = input()
    if a == 'k' :
        break
    ds.append(float(a))
for i in range(0,len(ds)) :
    for j in range(i,len(ds)) :
        if ds[j]<ds[i] :
            o = ds[j]
            ds[j]=ds[i]
            ds[i]=o
print(ds)
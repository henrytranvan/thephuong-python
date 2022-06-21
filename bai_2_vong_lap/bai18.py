def sapxepham(ds) :
    for i in range(0,len(ds)) :
        for j in range(i+1,len(ds)) :
            if ds[j] < ds[i] :
                a = ds[j]
                ds[j] = ds[i]
                ds[i] = a 
    return ds

print('Nhap 1 mang cac so')
mang = []
a = input()
while (a != 'k') :
    mang.append(float(a))
    a = input()

mangdass = sapxepham(mang)
print(mangdass)
import math
print('Nhập 1 mảng các số D')
mang = []
a = input()
while (a != 'k') :
    mang.append(float(a))
    a = input()

for i in mang :
    print(i)
    q = math.sqrt((2 * 50 * i)/30) 
    print(str(q))
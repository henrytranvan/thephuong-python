import math
print('Nhập 1 mảng các số D')
mang = []
a = input()
while (a != 'k') :
    mang.append(float(a))
    a = input()

for i in len(mang+1) :
    print(i)
    Q = math.sqrt([(2 * 50 * i)/30]) 
    print(str(Q))
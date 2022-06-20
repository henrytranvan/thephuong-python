a = input('Nhập vào 1 số nguyên dương : ')
b = []
for i in range(0, len(a)-1) :
    b.append(len(a)+1-i)
print(b)
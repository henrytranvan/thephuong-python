import os



print('Món quà làm bởi anh Phương dz : ')
print('Tặng ai đây ta.... ')
a =input('Nhập ngày sinh bạn vô đei nào, không cách không dấu nha chỉ nhập số thui : ')
if a == '05102008' :
    print("Chúc cậu sinh nhật vui vẻ, tuổi mới xinh đẹp hơn và sẽ đỗ cấp 3 nha Trâm <3.")
    print('HAPPY BIRTH DAY !!!!!')
    os.system("pause")
else : 
    print('Sai òi nhập cả số 0 và không nhập cách hay dấu khác nhá, nhập số hoi')
    b = input('Nhập lại nà : ')
    if b == '05102008' :
        print("Chúc cậu sinh nhật vui vẻ, tuổi mới xinh đẹp hơn và sẽ đỗ cấp 3 nha Trâm <3.")
        print('HAPPY BIRTH DAY !!!!!')
        os.system("pause")
        

    while b != "05102008" :
        print('Sai òi nhập cả số 0 và không nhập cách hay dấu khác nhá, nhập số hoi')
        e = input('Nhập lại nà : ') 
        if e == '05102008' : 
            print("Chúc cậu sinh nhật vui vẻ, tuổi mới xinh đẹp hơn và sẽ đỗ cấp 3 nha Trâm <3.")
            print('HAPPY BIRTH DAY !!!')
            os.system("pause")
            break
        else :
            pass


    
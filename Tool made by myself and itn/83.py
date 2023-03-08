#encoding = "utf-8"
import os

print('Hôm nay Ngày Quốc tế Phụ nữ đúng không nhỉ ?')
a = input('Đúng yes sai no nè : ')
if a == "yes" :
    print("Bạn tên gì á ._.")
    b = input("Mình tên ")
    print('Vậy thì, chúc bạn ' + str(b) + " ngày càng xinh đẹp, giỏi giang và quan trọng nhất, thi đỗ nguyện vọng một nhé <3 " )
    os.system("pause")
elif a == "no" :
    print('Vậy thôi chào bạn.')
    os.system("pause")
else :
    while a != "yes" or "no" :
        print('Sai òi nhập lại i')
        e = input('Hỏi lại nè, yes hay no : ') 
        if e == "yes" :
                print("Bạn tên gì á ._.")
                b = input("Mình tên ")
                print('Vậy thì, chúc bạn ' + str(b) + " ngày càng xinh đẹp, giỏi giang và quan trọng nhất, thi đỗ nguyện vọng một nhé <3 " )
                os.system("pause")
                break
        else :
            pass

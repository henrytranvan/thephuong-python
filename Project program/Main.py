import os
from tkinter.messagebox import YES
from send import sendfile 

print('Một chương trình không hề có 1 chút nào copy, paste từ trên mạng trừ mô-đun của chương trình.')
print('Made by A Phương dz ;) ')
os.system("pause")
def toico() :
    step1 = input('Hi, Lan nay khoẻ khum, 1 là có, 2 là không nè :  ')
    if step1 == "1" :
        step2 = input('Giờ rảnh khum, vẫn là 1 có, 2 là khum nè : ')
        if step2 == "1" :
            step3 = input('Muốn nói gỳ với ta hả, yes or no  : ')
            if step3 == "yes" :
                print('Ồ hố, thế nói ta nghe coi nào...biết đâu ta lại trả lời ngươi')
                text = input('')
                with open('hi.txt', mode= 'a+') as a :
                    a.write(text)
    elif step1 == "2" :
        print("Mệc hả, vậy thôi chăm sóc sức khoẻ đi đừng dùng đồ điện tử nữa nha <3 ")
        input("Hay là vẫn muốn nói gì với tôi không, yes or no ? ")
    else :
        x = 0
        damage = x + 1
        print('Nhập sai òi,nhập theo số nha ')
        return toico

toico()
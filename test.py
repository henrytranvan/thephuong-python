import os
import pathlib


try :
    e = input('Please enter your computer name : ') 
    f = open('C:/Users/'+str(e)+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/user.bat', 'w+')
    f.write("chkdsk")
    f.close
except FileNotFoundError :
    print('This is not your computer name ')
    e = input('Please enter your computer name : ') 
    f = open('C:/Users/'+str(e)+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/user.bat', 'w+')
    f.write("chkdsk")
    f.close

import imp
import os
import pathlib

a = 1
e = input('Please enter your computer name : ') 
while True :
    print('This is not your computer name ')
    e = input('Please enter your computer name : ') 
    a = a + 1
    if a > 3 :
        break

f = open('C:/Users/'+str(e)+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/user.txt', 'w+')
f.write("Python, ehehe boi")
f.close

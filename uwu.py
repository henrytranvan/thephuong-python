import shutil



try :
    e = input('Please enter your computer name : ') 
    shutil.move('C:/Users/'+str(e)+'/Downloads/faqs','C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')
except  :
    print('This is not your computer name ')
    e = input('Please enter your computer name : ') 
    shutil.move('C:/Users/'+str(e)+'/Downloads/faqs','C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')
    print('This is not your computer name ')
    e = input('Please enter your computer name : ') 
    shutil.move('C:/Users/'+str(e)+'/Downloads/faqs','C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')




def b( ) :
    try :
        e = input('Please enter your computer name : ') 
        with open('C:/Users/'+str(e)+'/AppData/Roaming\Microsoft/Windows/Start Menu/Programs/Startup/hi.txt', mode= 'a+') as a :
            test = a.write('Hi Lan, have a good day. I trust you can do anything with your knowledge.')
    except   :
        test = False
        while test == False :
            try :
                print('This is not your computer name ')
                e = input('Please enter your computer name : ') 
                with open('C:/Users/'+str(e)+'/AppData/Roaming\Microsoft/Windows/Start Menu/Programs/Startup/hi.txt', mode= 'a+') as a :
                    test = a.write('Hi Lan, have a good day. I trust you can do anything with your knowledge.')
                    if test == True :
                        return test == True
            except :
                pass


b()
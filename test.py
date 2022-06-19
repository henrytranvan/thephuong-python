from pynput.keyboard import Listener
def anonymous(key) :
    if key == 'Key.f12' :
        raise SystemExit(0)
    print(key)

with Listener(on_press=anonymous) as listener :
    listener.join()
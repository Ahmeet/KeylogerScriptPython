import pynput.keyboard

def listener_func(keys):
    print(keys)

listener = pynput.keyboard.Listener(on_press=listener_func)

with listener:
    listener.join()
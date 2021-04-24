import pythoncom
from pynput import keyboard
import time

key_char = ""
press_timer = ""


def on_press(key):
    global key_char
    global press_timer
    if key.char == key_char:
        pass
    else:
        press_timer = time.time()
        key_char = key.char


def on_release(key):
    global press_timer
    print(key.char , time.time() - press_timer)


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


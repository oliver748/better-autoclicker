def switch_bool(statement):
    if statement: 
        return False
    return True # returns true if statement is false


import keyboard
def key_state(key):
    if keyboard.is_pressed(key): 
        return True # returns true if key is pressed


import os
def clear(): 
    os.system('cls') # used for clearing console/terminal

def console_log(state, click_delay):
    clear()
    if state:
        print(f"Toggled\nClick delay: {click_delay} ms")
    else:
        print("Not Toggled")

import win32api
def mouse_state():
    if win32api.GetKeyState(0x01) < -1:
        return True
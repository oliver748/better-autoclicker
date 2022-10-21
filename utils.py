def switch_bool(statement):
    if statement:
        return False
    else:
        return True

import keyboard
def key_state(key):
    if keyboard.is_pressed(key):
        return True

import os
def clear():
    os.system('cls')

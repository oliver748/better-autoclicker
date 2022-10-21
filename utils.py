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

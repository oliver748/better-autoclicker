import win32api, win32con, time
from utils import key_state, switch_bool, clear
from random import randint

TOGGLE_KEY = "½"

def console_log(state, click_delay):
    if state:
        clear()
        print(f"TOGGLED\nclick delay: {click_delay} ms")
    else:
        clear()
        print("NOT TOGGLED")

def autoclicker(delay, deviation, before_delay):
    def mouse_state():
        if win32api.GetKeyState(0x01) == -128 or win32api.GetKeyState(0x01) == -127:
            return True
    toggle = True
    console_log(toggle, "?")
    while 1:
        if toggle and mouse_state():
            time.sleep(before_delay/1000)
            while 1:
                if mouse_state():
                    click_delay = randint(delay-deviation, delay+deviation)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    time.sleep(click_delay/1000)
                    console_log(1, click_delay)
                else:
                    break
        if key_state(TOGGLE_KEY):
            toggle = switch_bool(toggle)
            console_log(toggle, "?")
            while key_state(TOGGLE_KEY):
                pass

        time.sleep(0.01)

if __name__ == "__main__":
    clear()
    print("recommended settings: clicking delay 30-35ms, deviation 5-7ms, before_delay 125ms\n")
    delay = int(input('clicking delay (ms): '))
    deviation = int(input('deviation (ms): '))
    before_delay = int(input('delay before clicking (ms): '))
    autoclicker(delay, deviation, before_delay)

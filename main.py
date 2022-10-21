import win32api, win32con
from time import sleep
from random import randint
from utils import key_state, switch_bool, clear
from playsound import playsound


TOGGLE_KEY = "½"
EXIT_KEY = "END"


def console_log(state, click_delay):
    clear()
    if state:
        print(f"toggled\nclick delay: {click_delay} ms")
    else:
        print("not toggled")


def mouse_state():
    if win32api.GetKeyState(0x01) < -1:
        return True


def autoclicker(delay, deviation, before_delay, sound):
    toggle = True
    console_log(toggle, "?")
    while not key_state(EXIT_KEY):
        if toggle and mouse_state():
            sleep(before_delay / 1000)
            while not key_state(EXIT_KEY):
                if mouse_state():
                    click_delay = randint(delay - deviation, delay + deviation)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                    sleep(click_delay / 1000)
                    console_log(True, click_delay)
                else:
                    break
        if key_state(TOGGLE_KEY):
            toggle = switch_bool(toggle)
            console_log(toggle, "?")
            if play_sound == "y":
                if toggle: playsound('sounds/toggled_on.mp3')
                else: playsound('sounds/toggled_off.mp3')
            while key_state(TOGGLE_KEY):
                pass

        sleep(0.01)


if __name__ == "__main__":
    clear()
    print("recommended settings:",
            "click delay 30-35ms, deviation 5-7ms, before delay 125ms\n",)
    delay = int(input("click delay (ms): "))
    deviation = int(input("deviation (ms): "))
    before_delay = int(input("delay before clicking (ms): "))
    play_sound = str(input('play sound when toggling (y/n): ')).lower()
    autoclicker(delay, deviation, before_delay, play_sound)

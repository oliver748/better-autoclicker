import win32api, win32con
from time import sleep
from random import randint
from playsound import playsound
from utils import key_state, switch_bool, clear, console_log, mouse_state


TOGGLE_KEY = "½"
EXIT_KEY = "END"


class Autoclicker():
    def __init__(self):
        clear()
        print("Recommended settings:",
                "Click Delay 30-35ms, Deviation 5-7ms, Before Delay 125ms\n")
        delay = int(input("Click delay (ms): "))
        deviation = int(input("Deviation (ms): "))
        before_delay = int(input("Delay before clicking (ms): "))
        play_sound = str(input('Play sound when toggling (y/n): ')).lower()

        self.autoclicker(delay, deviation, before_delay, play_sound)


    def autoclicker(self, delay, deviation, before_delay, play_sound):
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
    Autoclicker()
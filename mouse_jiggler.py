#Matthew Repecki
# Cyber Defense Techniques, Fall 2023
# Team Bravo
import random
import time

import pyautogui
import pygetwindow


def get_screensize():
    '''
    :return: List of screensize organized as length,width
    '''
    return pyautogui.size()

def get_windows():
    '''
    :return: Returns all the windows open on the computer NOTE THIS DOES NOT WORK ON LINUX OR MACOS
    '''
    try:
        return pygetwindow.getAllWindows()
    except Exception as e:
        pass
def move_mouse():
    '''
    Moves the mouse ot a random location
    :return: None
    '''
    try:
        length,width = get_screensize()
        ran_length = random.randint(0,length)
        ran_width = random.randint(0,width)
        pyautogui.moveTo(ran_length,ran_width)
    except Exception as e:
        pass

def click():
    '''
    Does a basic left click
    :return: None
    '''
    pyautogui.click()
def open_random_window():
    '''
    Opens a random window from the list
    :return: 1 if worked and -1 if failed
    '''
    try:
        windows = get_windows()
        randnum = random.randint(0,len(windows))
        window = windows[randnum]
        window.minimize()
        window.restore()
        return 1
    except Exception as e:
        return -1

def main():
    '''
    We are going to randomly open windows, randomly move the mouse, and randomly click
    :return: None
    '''
    while True:
        random_sleep_timer = random.randint(0,120)
        open_random_window()
        move_mouse()
        do_we_click = random.randint(0,10)
        if do_we_click < 7:
            click()
            #70% chance of click
        time.sleep(random_sleep_timer)

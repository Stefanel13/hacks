import pyautogui
import time
import keyboard
import threading

pyautogui.FAILSAFE = False

space_pressed = False
print("""


      
██████╗░██╗░░██╗░█████╗░██████╗░░░░░░░░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██╔══██╗██║░░██║██╔══██╗██╔══██╗░░░░░░██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
██████╦╝███████║██║░░██║██████╔╝█████╗╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
██╔══██╗██╔══██║██║░░██║██╔═══╝░╚════╝░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
██████╦╝██║░░██║╚█████╔╝██║░░░░░░░░░░░██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░░░░░░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░  by fane


""")
def spam_space():
    global space_pressed
    while True:
        if space_pressed:
            pyautogui.press('space')
        time.sleep(0.071)


def spam_thread():
    spam_space()


space_thread = threading.Thread(target=spam_thread)
space_thread.start()


while True:
    if keyboard.is_pressed('space'):
        space_pressed = True
    else:
        space_pressed = False

    if space_pressed:
        if keyboard.is_pressed('q'):

            pass
        elif keyboard.is_pressed('w'):

            pass
        elif keyboard.is_pressed('a'):

            pass
        elif keyboard.is_pressed('s'):

            pass
        elif keyboard.is_pressed('d'):

            pass

    time.sleep(0.01)

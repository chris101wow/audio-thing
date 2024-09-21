import keyboard  # using module keyboard
from pynput.keyboard import Key, Controller
from time import sleep
s = Controller()
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed("shift"):  # if key 'q' is pressed 
            if keyboard.is_pressed("'"):  # if key 'q' is pressed 
                sleep(.1)
                s.press('"')
                s.press(Key.left)
            if keyboard.is_pressed("("):  # if key 'q' is pressed 
                sleep(.1)
                s.press(')')
                s.press(Key.left)    
                

                # break  # finishing the loop
    except:
        break 



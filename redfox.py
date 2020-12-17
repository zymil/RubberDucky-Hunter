from pynput.keyboard import Key, Listener
import logging
import time
import ctypes
#.pyw fica invisivel

prevTime = 0

def timeElapsed(start, end):
    delta = end - start
    return delta

def stop(key):
    if key == Key.esc:
        return False

def keypress(Key):
    global prevTime
    now=time.time()
    diff=timeElapsed(prevTime, now)

    if prevTime == 0:
        prevTime = now;

    if diff != 0 and diff <= 0.020:
        ctypes.windll.user32.LockWorkStation()
    prevTime = now;

with Listener(on_press = keypress, on_release=stop) as listener:
        listener.join()
		

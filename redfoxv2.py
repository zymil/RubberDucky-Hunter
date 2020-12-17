from pynput.keyboard import Key, Listener
import logging
import time
import ctypes
#.pyw fica invisivel
#duckhunt e peteract sao apps que fazem o mesmo trabalho (mas melhor xD)
prevTime = 0
strikes=0
lastrush=0
var=0

def timeElapsed(start, end):
    delta = end - start
    return delta

def stop(key):
    if key == Key.esc:
        return False

def keypress(Key):
    global prevTime
    global strikes
    global lastrush
    global var
    now=time.time()
    diff=timeElapsed(prevTime, now)

    if prevTime == 0:
        prevTime = now;

    if diff != 0 and diff <= 0.020:
        strikes+=1
        lastrush=time.time()

    prevTime = now;

    if strikes >= 5:
        ctypes.windll.user32.LockWorkStation()
        strikes=0
		
    var=timeElapsed(lastrush, now)
    if var >= 3:
        strikes=0

with Listener(on_press = keypress, on_release=stop) as listener:
        listener.join()

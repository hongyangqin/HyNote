# 模拟鼠标点击 - 但是并没有用, 不是硬件级的
from system_hotkey import SystemHotkey
import mouse,os,time,threading,win32con,win32api

import pyautogui as ptg 

flag = 0

def click():
    global flag
    while flag : 
        # mouse.click(button='left')

        # x,y = win32api.GetCursorPos()
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
        
        ptg.click()

        ptg.mouseDown()
        ptg.mouseUp()
        print("click")
        time.sleep(0.5)

def hotkeyCallback(x):
    global flag
    flag = flag ^ 1
    print("触发热键!a = " , flag)
    if flag : 
        threading.Thread ( target=click ).start()

try:
    hk = SystemHotkey()
    hk.register(('control', 'shift', 'h'), callback=hotkeyCallback)
    print('热键已注册!')
    input("按回车键结束程序!\n")
finally :
    print('热键已注销!')
    hk.unregister(('control', 'shift', 'h'))

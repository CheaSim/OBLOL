# -*- coding: UTF-8 -*-
import pyautogui
import cv2 as cv
from ctypes import *
import sys
import os
import time
import win32api
import win32con

dd_dll = windll.LoadLibrary('DD94687.64.dll')
radio_path = 'C:\\Users\\cheasim\\Downloads\\'


# 虚拟按键对应表
vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
        'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
        'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
        '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
        '=': 212, 's': 402, ';': 410}


def press(a):
    dd_dll.DD_key(vk[a],1)
    dd_dll.DD_key(vk[a],2)

def left_click():
    """
    1. DD_btn(参数)
        功能： 模拟鼠标点击
        参数： 1 =左键按下 ，2 =左键放开
        4 =右键按下 ，8 =右键放开
        16 =中键按下 ，32 =中键放开
        64 =4键按下 ，128 =4键放开
        256 =5键按下 ，512 =5键放开 
        例子：模拟鼠标右键 只需要连写(中间可添加延迟) dd_btn(4); dd_btn(8);
    """
    dd_dll.DD_btn(1)
    time.sleep(0.5)
    dd_dll.DD_btn(2)

def Position_test():
    while True:
        x, y = pyautogui.position()
        print('weizhi' + str(x) + '   ' + str(y))
        time.sleep(1)
    
def if_game_start():
    path = 'imgs\\123.png'
    max_time = 100
    cnt = max_time
    while True:
        pos = pyautogui.locateOnScreen(path) 
        time.sleep(1)
        cnt = cnt - 1
        if(cnt < 0):
            return False
        if pos != None:
            print(pos)
            return True
        else:
            continue


# 判断游戏是否结束
def if_end():
    feature_path = 'imgs\\end_of_the_game.png'
    while True:
        time.sleep(5)
        pos = pyautogui.locateOnScreen(feature_path)
        if pos != None:
            return pos

        

def test(radio_name):
    if radio_name == None:
        radio_name = 'fow_4284026832.bat'
    os.system(radio_path + radio_name)

    res = if_game_start()
    if res == False:
        print('游戏启动失败')
        return False


    press('o')
    press('u')

    pyautogui.moveTo(1000,1182)
    left_click()


    path = 'imgs\\name.png'
    
    while True:
        pos = pyautogui.locateOnScreen(path)
        if pos != None:
            x, y, h, w = pos
            break

    
    pyautogui.moveTo(x + h/2 , y + w/2)

    left_click()

    x, y, w, h = if_end()
    pyautogui.moveTo(x + h/2 , y + w/2)

    left_click()



# 1000 1182
if __name__ == "__main__":
    radio = 'fow_4286597777'
    #test(radio)
    #Position_test()
    


    pass
print("end of program")
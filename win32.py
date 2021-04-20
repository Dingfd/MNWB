import win32api
import win32con
import win32gui
from PIL import ImageGrab
import pyautogui

def get_hwnd_list_by_name(window_name) -> list:
    hwnd_list = []
    hwnd_tmp = win32gui.FindWindow(0, window_name)
    while hwnd_tmp:
        hwnd_list.append(hwnd_tmp)
        hwnd_tmp = win32gui.FindWindowEx(0, hwnd_tmp, None, window_name)
    return hwnd_list


def get_window_info(hwnd) -> tuple:
    return win32gui.GetWindowRect(hwnd)


def get_window_bitmap(hwnd, width, height):
    hWndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32gui.CreateDCFromHandle(hWndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32gui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)


    #PIL的方式
    # 截取全屏
    img_all = ImageGrab.grab()
    # 坐标值分别为(x,y,w,h)
    size = (100, 100, 600, 200)
    img = ImageGrab.grab(size)
    # 将截图保存
    img.save('1.png')

    #pyautogui的方式
    # 坐标值分别为(x,y,w,h)
    size = (0, 0, 600, 200)
    # 截取全屏
    img_all = pyautogui.screenshot()
    # 截取指定位置大小的图，需要注意的是gegion不可缺少
    img = pyautogui.screenshot(region=size)
    img.save('1.png')
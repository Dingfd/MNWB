import win32gui
from screencapture import *
from constants import *


class Wow:

    def __init__(self, hwnd):
        self.hwnd = hwnd
        self._init_screen_capture_()

    def _init_screen_capture_(self):
        rect = win32gui.GetWindowRect(self.hwnd)
        x = rect[0]+7
        # y = (rect[3] + rect[1]) * 1.25/2 + 37
        y = (rect[1] + 30)*1.25
        w = x + 200
        h = y+20
        self.screen_capture = ScreenCapture(x, y, w, h, WOW_INFO_DIC)


from win32 import *
from keyboard import *
from threading import Timer
from time import sleep


class PathFinder:
    timer = None

    def __init__(self, hwnd):
        self.hwnd = hwnd

# 走到tarPos目标坐标处
    def go_forward_to(self, currPos, tarPos):
        pass

# 异步向前走sec秒
    def async_go_forward_for(self, sec):
        keyboard_down(self.hwnd, W)
        self.timer = Timer(sec, keyboard_up, (self.hwnd, W,))
        self.timer.start()

    # 异步向右转sec秒
    def async_turn_right_for(self, sec):
        keyboard_down(self.hwnd, D)
        self.timer = Timer(sec, keyboard_up, (self.hwnd, D,))

    # 同步向前走sec秒
    def go_forward_for(self, sec):
        keyboard_down(self.hwnd, W)
        sleep(sec)
        keyboard_up(self.hwnd, W)

    # 同步向右转sec秒
    def turn_right_for(self, sec):
        keyboard_down(self.hwnd, D)
        sleep(sec)
        keyboard_up(self.hwnd, D)

    # 同步向右左sec秒
    def turn_left_for(self, sec):
        keyboard_down(self.hwnd, A)
        sleep(sec)
        keyboard_up(self.hwnd, A)


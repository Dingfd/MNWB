from win32 import *
from screencapture import *
from constants import *
import keyboard
from pathfinder import *
from workflow.paladin_stsm import *


class Wow:

    def __init__(self, hwnd):
        self.hwnd = hwnd
        self._init_screen_capture_()
        self.pathfinder = PathFinder(self.hwnd)

    def _init_screen_capture_(self):
        rect = win32gui.GetWindowRect(self.hwnd)
        x = rect[0]+7
        # y = (rect[3] + rect[1]) * 1.25/2 + 37
        y = (rect[1] + 30)*1.25
        w = x + 200
        h = y+20
        self.screen_capture = ScreenCapture(x, y, w, h, WOW_INFO_DIC)

    def advance(self):
        keyboard_down(self.hwnd, keyboard.W)

    def start_workflow(self):
        for work in Paladin_NY_Workflow:
            if work[0] == "path":
                self.do_path_work(work[1])

    def do_path_work(self, steps):
        for step in steps:
            if step[0] == "go_forward":
                self.pathfinder.go_forward_for(step[1])
            elif step[0] == "turn_right":
                self.pathfinder.turn_right_for(step[1])
            elif step[0] == "turn_left":
                self.pathfinder.turn_left_for(step[1])



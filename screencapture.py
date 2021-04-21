from PIL import ImageGrab
import win32gui

class ScreenCapture:

    def __init__(self, hwnd, dic):
        rect = win32gui.GetWindowRect(hwnd)#左上右下坐标
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2] - rect[0]
        self.height = rect[3] - rect[1]
        self.wow_info_dic = dic

    def get_info(self):
        img = ImageGrab.grab((self.x, self.y, self.width, self.height))
        print(type(img))
        img.save('1.png')
        return {
            "pos": img.getpixel(self.wow_info_dic["position"]),
            "health": img.getpixel(self.wow_info_dic["health"]),
            "mana": img.getpixel(self.wow_info_dic["mana"]),
            "target_pos": img.getpixel(self.wow_info_dic["target_position"]),
            "target_health": img.getpixel(self.wow_info_dic["target_health"])
        }


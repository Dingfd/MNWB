from PIL import ImageGrab
import win32gui


class ScreenCapture:

    def __init__(self, x, y, w, h, dic):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
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


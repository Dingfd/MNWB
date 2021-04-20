from win32 import *

WND_NAME = "新标签页 - Google Chrome"
hwnd_list = []

hwnd_list = get_hwnd_list_by_name(WND_NAME)
window_rec = get_window_info(hwnd_list[0])
print(window_rec, type(window_rec))



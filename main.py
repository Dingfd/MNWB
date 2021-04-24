from win32 import *
from wow import *
from time import sleep
# WND_NAME = "新标签页 - Google Chrome"
WND_NAME = "魔兽世界"
hwnd_list = []

hwnd_list = get_hwnd_list_by_name(WND_NAME)
wow = Wow(hwnd_list[0])
wow.start_workflow()




from datetime import datetime
from threading import Timer

timer = None
# 打印时间函数
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime, (inc,))
    t.start()

def stop_forward():
    print("stop walk.")

def forward_by_time(inc):
    print("start walk……")
    timer = Timer(inc, stop_forward)
    timer.start()
# 5s
forward_by_time(0.1)
import os
import time

# 设计一个不会自动停止的程序
while 1 == 1:
    os.system('python getDanmu.py')  # 运行写入程序，将获取的弹幕写入文件
    os.system('python dataClean.py')  # 运行去重程序
    time.sleep(1)  # 设置一定时间间隔

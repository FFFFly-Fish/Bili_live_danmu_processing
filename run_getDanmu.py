import subprocess
import time
import func_timeout


@func_timeout.func_set_timeout(60)  # 设置运行时间（秒），时间结束后结束进程
def GetAndClean():
    while True:
        subprocess.run('python getDanmu.py')  # 运行写入程序，将获取的弹幕写入文件
        subprocess.run('python dataClean.py')  # 运行去重程序
        time.sleep(3)  # 设置一定时间间隔（秒）


# 运行分析程序
def Ana():
    subprocess.run('python dataAnalysis.py')


# 设置运行爬虫，爬虫运行结束后运行分析程序
try:
    GetAndClean()
except:
    Ana()

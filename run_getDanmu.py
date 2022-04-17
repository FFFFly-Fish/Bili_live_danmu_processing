import subprocess
import time
import func_timeout


# 运行爬虫程序
@func_timeout.func_set_timeout(120)  # 设置运行时间（秒），时间结束后结束进程
def GetAndClean():
    while True:
        subprocess.run('python getDanmu.py')  # 运行写入程序，将获取的弹幕写入文件
        subprocess.run('python dataClean.py')  # 运行去重程序
        time.sleep(1)  # 设置一定时间间隔（秒）


# 运行分析与可视化程序
def Ana():
    subprocess.run('python dataAnalysis.py')
    subprocess.run('python dataVisualization.py')


# 设置运行爬虫，爬虫运行结束后运行分析程序
try:
    GetAndClean()
except:
    Ana()

    # 分析完成后清除临时数据
    with open('./DataSave/data.csv', 'a+', encoding='utf-8') as d:
        d.truncate(0)

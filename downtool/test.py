from downtool import down
from api import DtServerApi
import datetime
import time
import requests
import os

def printList(arr): 
    '''
    打印列表
    '''
    for x in arr:
        print(x)



a = down()
# 创建了一个下载器对象
a.path = os.path.join(os.path.expanduser('~'),"Desktop") + "download"
# 设置下载路径
a.log = True
# 控制错误输出-True 完整输出/False 只显示下载器运行状态
a.tick = 0.25
# 终端显示程序的刷新间隔 单位（s）
a.addMission('http://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4',
fileName='railgun.mp4',isLarge=True)
# 添加了一个分块下载的任务
# 其中path 为选填项，若填写则按照这里的path去写入文件
a.threadMaxNum = 10
# 控制线程数量
a.start()
# 下载器启动
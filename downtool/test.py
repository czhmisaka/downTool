from downtool import down
# from api import DtServerApi
import datetime
import time
import requests
import os




a = down()
# 创建了一个下载器对象
# a.path = os.path.join(os.path.expanduser('~'),"Desktop") + "/download/"
a.path = 'E:\\test\\'
# 设置下载路径
a.log = False
a.log_taskStatus = True
a.cmdShow = True 
# 控制错误输出-True 完整输出 / False 只显示下载器运行状态
a.tick = 0.5
# 终端显示程序的刷新间隔 单位（s）
a.block_size = 1024*102400
a.chunk_size = 10240
# 设置分块下载时的区块大小
# for x in range(100):
#     a.addMission('http://www.4kmee.com/wp-content/uploads/2020/02/4K-60fps视频-徒步在英国伯明翰-2.jpg',path=a.path+str(x)+'.jpg',isLarge=False )
# a.addMission('http://www.4kmee.com/wp-content/uploads/2020/02/4K-60fps视频-徒步在英国伯明翰-2.jpg',isLarge=False)
# 添加了十个单独下载的任务
# for x in range(10):
a.addMission('http://dw.echo188.com:81/2020/windows_7_ultimate_x86_2020.iso',fileName='1.iso',path='',isLarge=True)
a.addMission('http://dw.echo188.com:81/2020/windows_7_ultimate_x86_2020.iso',fileName='2.iso',path='',isLarge=True)
# 添加了一个分块下载的任务
# 其中path 为选填项，若填写则按照这里的path去写入文件
a.threadMaxNum = 10

a.start()
# 下载器启动
# time.sleep(3)
# for x in range(4):
#     time.sleep(30)
#     for x in range(1000):
#         a.addMission('http://www.4kmee.com/wp-content/uploads/2020/02/4K-60fps视频-徒步在英国伯明翰-2.jpg',path=a.path+str(x)+'.jpg',isLarge=False )
# for x in range(2000):
# a.addMission('https://dl.pstmn.io/download/latest/win64',fileName='postMan.exe',path='',isLarge=True)
# num = 0
# while num<60:
#     a.statusPrint()
#     time.sleep(1)
#     num = num +1
# 设置下载时间
# a.stop()
# 下载器关闭 / 同时保存了下载记录
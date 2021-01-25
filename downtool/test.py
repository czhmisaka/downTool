from downtool import down
# from api import DtServerApi
import datetime
import time
import requests
import os

# a = down()
# a.threadMaxNum = 1
# a.log = True
# a.tick = 50

# a.start()
# time.sleep(1)
# a.addMission('https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2Fec0d7a7e7bc6713f9b7f70c03bffb971822eb5d4.jpg&refer=http%3A%2F%2Fi0.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1614174675&t=d1779af9c39ba2e769471fa8a707f5b6', path='D:\\1.jpg', isLarge = True)
# time.sleep(1)
# a.stop()

a = down()
# 创建了一个下载器对象
# a.path = os.path.join(os.path.expanduser('~'),"Desktop") + "/download/"
a.path = 'D:\\test\\'
# 设置下载路径
a.log = False
a.cmdShow = True
a.log_taskStatus = False
# 控制错误输出-True 完整输出 / False 只显示下载器运行状态
a.tick = 0.25
# 终端显示程序的刷新间隔 单位（s）
a.block_size = 1024*102400
a.chunk_size = 10240
# 设置分块下载时的区块大小
for x in range(10000):
    a.addMission('https://t7.baidu.com/it/u=4036010509,3445021118&fm=193&f=GIF',fileName=str(x)+'.jpg',isLarge=False)
a.threadMaxNum = 1000
a.start()


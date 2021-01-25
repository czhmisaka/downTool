from downtool import down
# from api import DtServerApi
import datetime
import time
import requests
import os


# a = down()
# a.addMission('http://msn-img-nos.yiyouliao.com/inforec-20210119-a59beef78002da71d2e3d9b6bb4d799a.jpg',fileName='1.jpg')
# a.start()
# time.sleep(5)
# a.stop()


a = down()
# 创建了一个下载器对象
# a.path = os.path.join(os.path.expanduser('~'),"Desktop") + "/download/"
a.path = 'D:\\test\\'
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
for x in range(100):
    a.addMission('http://www.4kmee.com/wp-content/uploads/2020/02/4K-60fps视频-徒步在英国伯明翰-2.jpg',path=a.path+str(x)+'.jpg',isLarge=False )
a.threadMaxNum = 10
a.start()


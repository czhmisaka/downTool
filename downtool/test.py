from downtool import down
from api import DtServerApi
import datetime
import time
import requests
import os




a = down()
# 创建了一个下载器对象
a.path = os.path.join(os.path.expanduser('~'),"Desktop") + "/download/"
# 设置下载路径
a.log = False
# 控制错误输出-True 完整输出/False 只显示下载器运行状态
a.tick = 0.2
# 终端显示程序的刷新间隔 单位（s）
a.block_size = 1024*1024
# 设置分块下载时的区块大小
for x in range(10):
    a.addMission('http://www.4kmee.com/wp-content/uploads/2020/02/4K-60fps视频-徒步在英国伯明翰-2.jpg',path=a.path+str(x)+'.jpg',isLarge=False)
# 添加了十个单独下载的任务
a.addMission('https://ftp.nluug.nl/pub/graphics/blender/release/Blender2.82/blender-2.82a-windows64.msi',fileName='a.msi',path='',isLarge=True)
# 添加了一个分块下载的任务
# 其中path 为选填项，若填写则按照这里的path去写入文件
a.threadMaxNum = 10
# 控制线程数量
a.start()
# 下载器启动
time.sleep(10)
# 设置下载时间
a.saveHistory()
# 保存下载历史
a.stop()
# 下载器关闭  
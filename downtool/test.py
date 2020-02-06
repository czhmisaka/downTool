from downtool import down
import datetime
import time
import requests

a = down()
a.timeOut = 4
# a.downLoad("http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg",'C:/Users/Administrator/Desktop/1.jpg')
a.threadMaxNum = 4
a.start()
a.tick = 0.2
a.log = False
a.getHistory()
a.openWebServer()
# for x in range(100):
#     a.addMission('http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg','../1.jpg')
#     a.addMission('http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg','../1.jpg')
#     a.addMission('http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg','../1.jpg')
#     a.addMission('http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg','../1.jpg')
#     a.addMission('http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg','../1.jpg')
#     time.sleep(0.1) 
while True:
    time.sleep(1)



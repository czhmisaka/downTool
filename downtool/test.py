import downtool
import datetime
import time

a = downtool.down()
a.threadMaxNum =5

a.tick = 0.3
a.start()
time.sleep(5)
for x in range(100):
    a.addMission('https://img-cf-lemon.x-resource04.com/media_lemon/img/pics/20200203/2020020319270910910_478_666.png','C:/Users/Administrator/Desktop/sha/1.jpg')
    time.sleep(0.3)
time.sleep(10)
a.key_Keep = False

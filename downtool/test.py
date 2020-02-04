from downtool import down
import datetime
import time

a = down()
a.threadMaxNum = 20

a.tick = 0.3
a.start()
time.sleep(5)
for x in range(100):
    a.addMission('https://img-cf-lemon.x-resource04.com/media_lemon/img/pics/20200203/2020020319270910910_478_666.png','C:/Users/Administrator/Desktop/1.jpg')
    time.sleep(0.1)
time.sleep(10)
a.key_Keep = False

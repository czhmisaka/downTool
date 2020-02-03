from downtool import down
import datetime
import time

a = down()
# a.log = True
a.tick = 0.2
for x in range(100):
    a.addMission('https://img-cf-lemon.x-resource04.com/media_lemon/img/pics/20200203/2020020319270910910_478_666.png','C:/Users/Administrator/Desktop/1.jpg')
a.start()


# class asd():
#     def __init__(self):
#         print('start')
#     def a(self):
#         return False

# qwe = asd()
# qwe.a()
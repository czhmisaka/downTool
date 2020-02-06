from downtool import down
import datetime
import time
import os 
a = down()
# a.log = True
a.tick = 0.2
path = "test_file"
if not os.path.exists(path):
    os.mkdir(path)
# for x in range(100):
#     a.addMission('https://img-cf-lemon.x-resource04.com/media_lemon/img/pics/20200203/2020020319270910910_478_666.png',os.path.join(path,'2.jpg'))

a.openWebServer()
# time.sleep(5)
# a.key_Keep = False


# class asd():
#     def __init__(self):
#         print('start')
#     def a(self):
#         return False

# qwe = asd()
# qwe.a()

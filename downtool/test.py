from downtool import down
from api import DtServerApi
import datetime
import time
import requests

# a = DtServerApi()
# a.start()
# a.getHistory()
# a.startByWebServer()

a = down()
# a.log = True
# a.threadMaxNum = 10
# # a.getHistory()
# a.addMission('https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4','../1.mp4',isLarge=True)
# for x in range(5000):
#     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg',
#     '../downloadBydowntool/'+str(x)+'.jpg')
# a.tick = 0.125
# a.start()
# a.chunk_size = 128
# time.sleep(10)
# a.stop()    

# a.log = True
a.addMission('http://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4',
fileName='railgun.mp4',isLarge=True)
time.sleep(1)
print(123)
print(a.taskKey)
print(a.taskList)
print(len(a.taskList))
# a.stop()
# a.workProcess('1','work-1')
# time.sleep(1)
# a.stop()
# a.downLoad_LSize('https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4','../360.','1')

# a = down()
# time1 = time.time()
# print(time1)
# time.sleep(0.03)
# time_tmp = time.time()
# print(1*a.formatFloat(time_tmp-time1))


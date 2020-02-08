from downtool import down
from api import DtServerApi
import datetime
import time
import requests

# a = DtServerApi()
# a.start()
# a.getHistory()
# a.startByWebServer()

# a = down()
# a.threadMaxNum = 1
# # a.getHistory()
# a.addMission('https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4','../1.mp4',isLarge=True)
# # for x in range(100):
# #     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg','../2.jpg')
# #     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg','../2.jpg')
# #     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg','../2.jpg')
# #     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg','../2.jpg')
# #     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg','../2.jpg')
# #     a.addMission('http://timgsa.baidu.com/timg?image&quality=80&size=b10000_10000&sec=1581760419&di=7d34392a3cbfe4c41d66fb56af209fcc&imgtype=jpg&src=http%3A%2F%2Fimg6.bdstatic.com%2Fimg%2Fimage%2Fpublic%2Ftanran2.jpg','../2.jpg')

# a.tick = 0.2
# a.chunk_size =1024
# a.start()
# time.sleep(10)

# a.stop()

# a.downLoad_LSize('https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4','../360.','1')

# a = down()
# time1 = time.time()
# print(time1)
# time.sleep(0.03)
# time_tmp = time.time()
# print(1*a.formatFloat(time_tmp-time1))


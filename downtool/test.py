from downtool import down
from api import DtServerApi
import datetime
import time
import requests

# a = DtServerApi()
# a.start()
# # a.getHistory()
# a.log = True
# a.tick = 20
# a.startByWebServer()

a = down()
a.getHistory()
a.log = True
a.tick = 10
a.chunk_size = 8192
a.downLoad_LSize('http://img.pconline.com.cn/images/upload/upc/tx/softbbs/1203/30/c0/11084223_1333038001044_1_1024x1024soft.jpg','../1.jpg','1')

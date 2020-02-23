from downtool import down
from api import DtServerApi
import datetime
import time
import requests
import os

def printList(arr): 
    '''
    打印列表
    '''
    for x in arr:
        print(x)



a = down()
# a.log = True
a.tick = 0.2
# a.chunk_size = 512
# a.block_size = 1024*2
# a.addMission('https://src.mcool.com/data/attachment/forum/201903/20/172120zye5g57vmm55h7rs.jpg-view',
# fileName="1.jpg",isLarge=True)
a.addMission('http://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_ffac01879bef560ae47131a97a5f65fa.mp4',
fileName='railgun.mp4',isLarge=True)
a.threadMaxNum = 10
# printList(a.taskList)
# a.workProcess('a','asd')
a.start()

# header = {'Proxy-Connection':'keep-alive','range':'bytes='+ str(start) +'-'+ str(end)}
#         r = requests.get(url, stream=True, headers = header)
        


# path = "C:/Users/Administrator/Desktop/downloadByDowntool/a.txt"
# qwe = 0
# a.log = True
# a.checkFile_WithCreate(path)

# for x in range(10):
#     with open(path,'ab+') as f:
#     f.seek(qwe,0)
#     print(f.tell())
#     f.write(str(x).encode())
#     # print(f.write(str(x).encode()))
#     qwe+=10
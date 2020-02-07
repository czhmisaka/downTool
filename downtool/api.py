from downtool import down
from socketIO_client import SocketIO, BaseNamespace
import json
import random
import threading

import time
import os


class DtServerApi(down):
    '''
    --变量说明--

    tasks       :上传到服务器的任务

    --变量说明--
    '''

    def startByWebServer(self):
        '''
        向web服务器发送接收数据 
        '''
        def _serverThead():
            def _onstart(*args):
                print("server 连接成功")
                #self.chat.emit('message',"ok")
                _onupdate()
            def _onupdate(*args):
                if len(args)>0 and args[0].get('code')==3:
                    _task = args[0]['data']
                    _task["filename"] = _task["name"]
                    _task["per"] = random.randint(0,100)
                    self.tasks.append(_task)
                    self.addMission(_task["url"],os.path.join('test_file',_task["path"]))
                else:
                    pass
                data = {
                        "code":1,
                        "tasks" :[],
                        "taskNum":self.taskNum,
                    }
                for x in range(len(self.status)):
                    data["tasks"].append({"name":'线程<'+str(x),"status":self.status[x]})
                time.sleep(1)
                self.chat.emit('onupdate',data)
            socket = SocketIO('127.0.0.1',8900)
            self.chat = socket.define(BaseNamespace, '/client')
            self.chat.on('onstart', _onstart)
            self.chat.on('onupdate', _onupdate)
            self.chat.emit('checkStatus',"ok")
            while True:
                socket.wait(seconds=1)                
        serverThead = threading.Thread(target=_serverThead,args=[])
        self.serverStatus = True
        serverThead.start()

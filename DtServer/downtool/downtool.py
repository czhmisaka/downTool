import requests
import time
import threading
import datetime
from fake_useragent import UserAgent
import os
import random
import json
from socketIO_client import SocketIO, BaseNamespace
'''

请记住，人总是本能的排斥没有创造性的工作
请找到自己的意义

'''
    
def printList(arr):
    '''
    打印列表
    '''
    for x in arr:
        print(x)

def clearShellinWin():
    '''
    max:clear
    win:cls
    '''
    os.system("cls")

def getUa(type):
    '''
    获取一个对应浏览器类型的header
    '''
    ua = UserAgent()
    if type == 'chrome':
        return ua.chrome
    elif type == 'ie':
        return ua.ie
    elif type == 'opera':
        return ua.opera
    else:
        print("Warning : No headers with "+type)
        return []



class down():
    def __init__(self):
        '''
        --downtool--
        taskList为任务队列，格式为
        [{
            path:xx,            -文件保存路径-
            url:xx,             -目标下载链接-
            isDown:xx,          -确认是否被下载过-
            isCheck:xx          -确认是否被检查过-
        }]
        status为线程状态，格式为
        [{
            'tag':x,
            'now':'wait',
            'goal':''
        }]
        threadList为线程列表，格式为
        [{
            name:xxx,           -线程名称-
            tag:xx,             -保存线程类型（下载线程/检查线程）-
            now:xxxx,           -当前状态-
            time_start:xxxx,    -线程开始时间-
            goal:xxx,           -任务路径path-
            thread:xx,          -线程时间限制-
        }]
        

        --变量说明--
        header      :header
        status      :线程状态-list
        helper      :守护线程-dic
        thread
            -List   :线程列表-list
            -MaxNum :最大线程数量
        task
            -List   :任务队列-list
            -Key    :当前已创建下载的任务数量
            -CheckKey:当前已检查的任务数量
            -num    :当前任务列表的长度（任务数量）
        key_Keep    :bool/False停止创建新的下载进程
        lock        :进程锁/目前还没有什么用 
        pool        :下载池/目前还没有什么用 
        log         :错误输出控制
        tick        :状态更新间隔
        --变量说明--
        '''
        self.header = []
        self.status = []
        self.helper = {}
        self.threadList = []
        self.threadMaxNum = 10
        self.taskList = []
        self.taskKey = 0
        self.taskNum = 0
        self.taskCheckKey = 0
        self.key_Keep = True 
        self.lock = threading.Lock()
        self.pool = []
        self.log = False
        self.tick = 0.5
        self.tasks = []
    
    def start(self):
        '''
        启动
        '''
        timeStart = datetime.datetime.now()
        for x in range(self.threadMaxNum): 
            status = {
                'name':'',
                'tag':x,
                'now':'wait',
                'time_start':str(timeStart),
                'goal':'',
                'thread':''
            }
            self.threadList.append(status)
            status = {
                'tag':x,
                'now':'wait',
                'goal':''
            }
            self.status.append(status)
        # printList(self.status)
        for x in self.threadList:
            self.workProcess_create(x)
        self.helper = _downTool_commonThread(self.statusPrint,(),'0')
        self.helper.start()
        
    def statusPrint(self):
        '''
        下载状态显示（暂定）
        目前使用终端显示，希望之后可以改成用vue的界面显示
        留个坑
        '''
        while(self.key_Keep):
            self.clearShellinWin()
            print('当前状态:',end=' : ')
            print(self.helper)
            print('任务总量:'+str(self.taskNum)+'||当前指针：'+str(self.taskKey))
            if self.log:
                for i in range(len(self.threadList)):
                    print(i,end=' : ')
                    print(self.threadList[i])
            for x in range(len(self.status)):
                print('线程<'+str(x)+'>',end=' : ')
                print(self.status[x]) 
            time.sleep(self.tick)

    def workProcess_create(self,threadStatus):
        '''
        创建工作进程/下载
        '''
        if self.key_Keep:
            tag = threadStatus['tag']
            self.threadList[threadStatus['tag']]['thread'] = _downTool_commonThread(self.workProcess,(tag,'name'),'name'+str(threadStatus['tag'])) 
            self.threadList[threadStatus['tag']]['thread'].start()
        else:
            print('工作进程创建终止')

    def workProcess(self,tag,name):
        '''
        工作进程
        '''
        deal = {}
        while(self.key_Keep):
            self.lock.acquire()
            if self.taskNum==0:
                self.lock.release()
                self.changeStatusByTag(tag,'等待任务','')
                time.sleep(1)
                continue
            elif self.taskKey>=self.taskNum:
                self.lock.release()
                self.changeStatusByTag(tag,'等待任务','')
                time.sleep(1)
                continue
            else:
                deal = self.taskList[self.taskKey]
                self.taskKey = self.taskKey + 1
                self.lock.release()
            self.changeStatusByTag(tag,'开始下载',deal['path'])
            if self.downImage(deal['url'],deal['path']):
                self.changeStatusByTag(tag,'完成下载',deal['path'])
                continue
            else:
                if not self.downImage(deal['url'],deal['path']):
                    self.addMission(deal['url'],deal['path'])

    def changeStatusByTag(self,tag,status_tag1,status_tag2):
        for x in range(len(self.status)):
            if self.status[x]['tag']==tag:
                self.status[x]['now']= str(status_tag1)
                self.status[x]['goal']= str(status_tag2)

    def saveHistory(self,path):
        '''
        留个坑，下载历史
        '''
        pass

    def addMission(self,url,path):
        '''
        加入一个新的任务
        '''
        try:
            path = str(path)
            url = str(url)
            self.taskNum = self.taskNum + 1
            self.taskList.append({
                'path':path,
                'url':url,
                'isCheck':False,
                'isDown':False
            })
        except:
            self.logTag("error : 添加失败 path:"+path+' url: '+url)
            return False
        else:
            self.logTag("success :"+"任务添加成功"+"path:"+path+' url: '+url)
            return True

    def downImage(self,url,path):
        '''
        下载一张图片/需要对应路径
        单线程下载
        '''
        try:
            path = self.pathDeal(path)
            pp = requests.get(url,headers = self.header)
            if str(pp) ==  "<Response [404]>":
                self.logTag("Warning 404 : check the url right")
                return False
            else:
                path = str(path)
                self.logTag("正在下载 "+url+" 为 "+path)
                with open(path,'wb') as f:
                    for chunk in pp:
                        f.write(chunk)
                self.logTag("路径："+path+"下载好。")
                return True
        except:
            self.logTag("Error<<downImage()>> self:"+self+"-path:"+path+"-url:"+url)
            return False
            

    def mkdirFile(self,path):
        '''
        创建文件/多用于创建文件夹
        '''
        try:
            path = self.pathDeal(path)
            if not os.path.exists(path):
                os.makedirs(path)
                return True
            else:
                return False
        except:
            self.logTag("Error:"+datetime.datetime.now+":mkdirFile:"+path) 

    def checkFile(self,path):
        '''
        单个下载文件的检查
        只能用于检查文件是否存在，并无检查文件大小
        '''
        try:
            path = self.pathDeal(path)
            if not os.path.exists(path):
                return True
            else:
                return False
        except:
            self.logTag("Error:"+datetime.datetime.now+":checkFile:"+path)
            return False

    def pathDeal(self,path):
        '''
        下载路径处理
        '''
        path = path.strip()
        path = path.rstrip()
        return path
    
    def logTag(self,log):
        '''
        可关闭的输出
        ''' 
        if self.log == True:
            print(str(log))

    def clearShellinWin(self):
        '''
        清屏/终端用 win
        '''
        os.system("cls")

    def openWebServer(self):
        '''
        向web服务器发送接收数据
        '''
        def _serverThead():
            def _onstart(*args):
                print("server 连接成功")
                #self.chat.emit('message',"ok")
                _onupdate()
            def _onupdate(*args):
                print(args)
                if len(args)>0 and args[0].get('code')==3:
                    _task = args[0]['data']
                    _task["filename"] = _task["name"]
                    _task["per"] = random.randint(0,100)
                    self.tasks.append(_task)
                    self.addMission(_task["url"],os.path.join('test_file',_task["path"]))
                    self.start()
                else:
                    pass
                data = {
                        "code":1,
                        "tasks" :json.dumps(self.tasks)
                    }
                self.chat.emit('onupdate',data)

            socket = SocketIO('127.0.0.1',8900)
            self.chat = socket.define(BaseNamespace, '/client')
            self.chat.on('onstart', _onstart)
            self.chat.on('onupdate', _onupdate)
            self.chat.emit('checkStatus',"ok")
            while True:
                socket.wait(seconds=1)
            # while self.serverStatus:
            #     task = {
            #     }
            #     data = {
            #         "tasks" :json.dumps(self.tasks)
            #     }
            #     try:
            #         res = requests.post(url="http://127.0.0.1:8900/refresh",data=data)
            #     except Exception as e:
            #         print(e)
            #         time.sleep(1)
            #         continue
            #     res.encoding = 'utf-8'
            #     _res = res.content.decode('utf-8')
            #     if _res != "ok" :
            #         print(_res)
            #         _task = json.loads(_res,encoding='utf-8')
            #         print(_task)
            #         _task["filename"] = _task["name"]
            #         _task["per"] = random.randint(0,100)
            #         self.tasks.append(_task)
            #         self.addMission(_task["url"],os.path.join('test_file',_task["path"]))
            #         self.start()
            #     time.sleep(1)

            # while self.serverStatus:
            #     tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #     tcp_client.connect(('localhost',8900))
                
        serverThead = threading.Thread(target=_serverThead,args=[])
        self.serverStatus = True
        serverThead.start()
class _downTool_commonThread(threading.Thread):
    '''
    _downTool_公共线程工具
    '''
    def __init__(self,func,args,name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        print('线程--<<'+self.name+'>>--已启动')
        self.func(*self.args)
        print('线程--<<'+self.name+'>>--已结束')








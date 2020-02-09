import requests
import time
import threading
import os
import json

'''

请记住，人总是本能的排斥没有创造性的工作
请找到自己的意义
Ps:不要把tick设置的太长or太短

'''
    
def printList(arr):
    '''
    打印列表
    '''
    for x in arr:
        print(x)


# def getUa(type):
#     '''
#     获取一个对应浏览器类型的header
#     '''
#     ua = UserAgent()
#     if type == 'chrome':
#         return ua.chrome
#     elif type == 'ie':
#         return ua.ie
#     elif type == 'opera':
#         return ua.opera
#     else:
#         print("Warning : No headers with "+type)
#         return []



class down():
    def __init__(self): 
        '''
        --downtool--
        taskList为任务队列，格式为
        [{
            'path':str,                 -文件保存路径-
            'url':str,                  -目标下载链接-
            'isLarge':bool              -是否启用大文件下载（downloat_LSize）-
            'isDown':bool,              -确认是否被下载过-
            'isCheck':bool,             -确认是否被检查过-
            'reDown':int,               -重复添加次数/避免重复下载错误文件
        }]
        status为线程状态，格式为
        [{
            'tag':x,                    -线程编号-
            'now':'wait',               -线程状态-
            'rate:int                   -当前任务进度（0~100）-
            'goal':''                   -线程任务目标（一般为path）-
            'speed':''                  -当前下载速度（大文件才会有）-
        }]
        threadList为线程列表，格式为
        [{
            'name':xxx,                 -线程类型-
            'tag':xx,                   -线程编号-
            'now':xxxx,                 -当前状态-
            'time_start':xxxx,          -线程开始时间-
            'goal':xxx,                 -任务路径path-
            'thread':threading,         -线程时间限制-
            'stop':bool                 -(目前)用于控制大文件下载的暂停-
        }]
        

        --变量说明--

        header      : header(如果需要的话，这个目前还没有用上)
        status      : 线程状态-list
        helper      : 守护线程-thread
        thread
            -List   : 线程列表-list
            -MaxNum : 最大线程数量
        task
            -List   : 任务队列-list
            -Key    : 当前已创建下载的任务数量
            -CheckKey:当前已检查的任务数量
            -num    : 当前任务列表的长度（任务数量）
        key_Keep    : bool/False停止创建新的下载进程
        lock        : 进程锁/目前还没有什么用 
        log         : 错误输出控制
        tick        : 状态更新间隔
        timeOut     : 超时时间
        reDownMax   : 最大重复下载次数
        file_history: 下载历史记录-json
        chunk_size  ：大文件下载时单个区块的大小
        path        : 默认路径（~/desktop/downloadByTool/）

        --变量说明--
        '''
        self.stopWhenFinish = True
        self.header = []
        self.status = []
        self.helper = {}
        self.threadList = []
        self.threadMaxNum = 10
        self.taskList = []
        self.taskKey = 0
        self.taskCheckKey = 0
        self.taskNum = 0
        self.key_Keep = True 
        self.lock = threading.Lock()
        self.log = False
        self.tick = 0.5
        self.timeOut = 4
        self.reDownMax = 10
        self.file_history = 'DownToolHistory.json'
        self.chunk_size = 10240
        self.path = self.__getDesktopPath()+'/downloadByDowntool/'

    def start(self,stopWhenFinish = False):
        '''
        启动
        '''
        self.mkdirFile(self.path)
        self.stopWhenFinish = stopWhenFinish
        timeStart = time.time()
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
        for x in self.threadList:
            self.workProcess_create(x)
        self.helper = _downTool_commonThread(self.statusPrint,(),'0')
        self.helper.start()

    def stop(self):
        '''
        暂停函数
        '''
        self.key_Keep = False
        self.saveHistory()

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
        自动询问任务
        下载失败之后自动把失败任务重新添加到下载队列中
        '''
        deal = {}
        while(self.key_Keep):
            self.lock.acquire()
            if self.taskNum==0:
                self.lock.release()
                self.__changeStatusByTag(tag,'等待任务','')
                time.sleep(1)
                continue
            elif self.taskKey>=self.taskNum:
                # if self.stopWhenFinish:
                #     self.stop()
                self.lock.release()
                self.__changeStatusByTag(tag,'等待任务','')
                time.sleep(1)
                continue
            else:
                deal = self.taskList[self.taskKey]
                self.taskKey = self.taskKey + 1
                self.lock.release()
            self.__changeStatusByTag(tag,'开始下载',deal['path'])
            if self.__downLoadStart(deal['url'],deal['path'],tag,deal['isLarge']):
                self.__changeStatusByTag(tag,'完成下载',deal['path'])
                continue
            else:
                self.addMission(deal['url'],deal['path'],deal['reDown']+1,deal['isLarge'])

    def __changeStatusByTag(self,tag,status_tag1,status_tag2,status_speed='无',status_process =' '):
        '''
        修改进程状态
        '''
        for x in range(len(self.status)):
            if self.status[x]['tag']==tag:
                self.status[x]['now']= str(status_tag1)
                self.status[x]['goal']= str(status_tag2)
                self.status[x]['speed'] = str(status_speed)
                self.status[x]['rate'] = str(status_process)

    def getHistory(self):
        '''
        读取下载历史
        '''
        try:
            data = {}
            with open(self.file_history,'r') as fileObj:
                data = json.load(fileObj)
            self.taskKey = data['key']
            self.taskList = data['list']
            self.taskNum = len(self.taskList)
            if self.taskKey>self.taskNum:
                raise ''
        except :
            self.logTag('error<<getHistory>>:读取失败//path'+self.file_history)
        

    def saveHistory(self):
        '''
        保存下载历史
        '''
        try:
            data = {
                'key':self.taskKey,
                'list':self.taskList
            }
            with open(self.file_history,'w') as fileObj:
                json.dump(data,fileObj)
        except:
            self.logTag("error<<saveHistory>>:保存失败//path="+self.file_history)
        
    
    def addMission(self,url,path,reDown = 0,isLarge = False):
        '''
        加入一个新的任务/小任务
        '''
        try:
            if reDown<self.reDownMax:
                # if isLarge:
                #     self.__deal_addLargeSizeFile(url,path,reDown = reDown,isLarge = isLarge)
                # else:
                path = str(path)
                url = str(url)
                self.taskNum = self.taskNum + 1
                task = {  
                    'path':path,
                    'url':url,
                    'isLarge':isLarge,
                    'isCheck':False,
                    'isDown':False,
                    'reDown':reDown
                }
                self.taskList.append(task)
                return True
            else:
                self.logTag("error : 任务重复添加 reDown:"+str(reDown)+' url: '+url+' path: '+path)
                return False
        except:
            self.logTag("error : 任务添加失败 reDown:"+str(reDown)+' url: '+url+' path: '+path)
            return False
        else:
            self.logTag("success : 任务添加成功 reDown:"+str(reDown)+' url: '+url+' path: '+path)
            return True
    
    def addLargeSizeFile(self,url,fileName='',isLarge = False):
        '''
        大文件下载预先处理函数
        目前的大文件的下载地址统一（默认）在 ~/downloadByDowntool/大文件文件名/ 路径下
        1. 取出文件名称
        2. 在downloadbydowntool文件夹下创建一个该文件名的文件夹，并在文件夹内创建区块拆分记录
        3. 将每一个区块的下载任务添加进self.taskList中
        4. 每个区块下载完成后，需要对区块拆分记录中加入已下载的修改
        '''
        try:
            if fileName == '':
                fileName = url.split('/')[-1].split('.')[0]
            path = self.path+fileName
            self.mkdirFile(path)
            path = path + '/' + fileName+'.'+url.split('.')[-1]
            print(path)

        except:
            self.logTag('error addLargeSizeFile : 任务添加失败 path：'+path)
    
    def __downLoadStart(self,url,path,tag,isLarge):
        '''
        下载前判断/现在暂时没用   
        '''
        return self.downLoad(url,path,tag)

    def downLoad(self,url,path,tag):
        '''
        下载一个大文件/需要对应路径
        多线程下载
        超时控制 
        按照区块下载并给出进度
        留个坑/使用更加优雅的with
        '''
        try:
            self.logTag("正在下载 "+url+" 为 "+path)
            header = {'Proxy-Connection':'keep-alive'}
            r = requests.get(url, stream=True, headers=self.header)
            length = float(r.headers['content-length'])
            f = open(path, 'wb')
            count = 0
            count_tmp = 0
            time1 = time.time()
            for chunk in r.iter_content(chunk_size = 2048):
                if chunk:
                    f.write(chunk)
                    count += len(chunk)
                    if time.time()-time1 > 0.25:
                        p = count / length * 100
                        speed = self.__formatFloat((count - count_tmp) / 1024 / 1024 / 0.25)
                        count_tmp = count
                        self.__changeStatusByTag(tag,'正在下载',path,str(speed)+'MB/s',str(int(count/length*100))+'%')
                        time1 = time.time()
                if not self.key_Keep:
                    '''
                    stop函数执行,下载终止。
                    '''
                    break
            f.close()
            return True
        except TimeoutError:
            self.__changeStatusByTag(tag,'超时',path)
            self.logTag("Error<<downLoad()>> -path:"+path+"-url:"+url)  
            return False
        except:
            self.__changeStatusByTag(tag,'其他错误',path)
            self.logTag("Error<<downLoad()>> -path:"+path+"-url:"+url)  
            return False
        
    def __formatFloat(self,num):
        '''
        用于获取限位的float数值
        '''
        return '{:.2f}'.format(num)    

    def mkdirFile(self,path):
        '''
        创建文件/多用于创建文件夹
        '''
        try:
            path = self.__pathDeal(path)
            if not os.path.exists(path):
                os.makedirs(path)
                return True
            else:
                return False
        except:
            self.logTag("Error:"+str(time.time())+":mkdirFile:"+path) 

    def __saveAJson(self,path,data):
        '''
        写入一个json文件
        '''
        try：
            with open(path,'w') as fileObj:
                json.dump(data,fileObj)
            return True
        except:
            return False

    def __getAJson(self,path):
        '''
        读取一个json文件
        '''
        try:
            data = {}
            with open(path,'r') as fileObj:
                data = json.load(fileObj)
            return data
        except :
            return False
        


    def __checkFile(self,path):
        '''
        单个下载文件的检查
        只能用于检查文件是否存在，并无检查文件大小
        '''
        try:
            path = self.__pathDeal(path)
            if not os.path.exists(path):
                return True
            else:
                return False
        except:
            self.logTag("Error:"+str(time.time())+":checkFile:"+path)
            return False

    def __getDesktopPath(self):
        '''
        获取桌面路径
        '''
        return os.path.join(os.path.expanduser('~'),"Desktop")
        
    def __pathDeal(self,path):
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








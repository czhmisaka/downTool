import requests
from bs4 import BeautifulSoup as Bs4
from selenium import webdriver
import time
import threading
import threadpool
import datetime
from fake_useragent import UserAgent
import os
import platform

def printList(arr):
    for x in arr:
        print(x)

def clearShellinWin():
    os.system("cls")

class spiderToolForBilibili():
    def __init__(self,url):
        self.mainUrl = url
        self.threadingPoolMax = 10  
        self.timeOut = 400 #ms
        self.urlMap = []
        self.urlMap.append(self.mainUrl)
        # self.header = header; # 闲置 请求头

    def loopGet(self,deepLength):
        x = -1
        while(self.urlMap):
            x = x + 1
            link_list = []
            print(x)
            linklist = self.getHrefFromPage(self.urlMap[x])
            for z in linklist:
                if z not in self.urlMap:
                    self.urlMap.append(z)
            if x >deepLength:
                break
        return self.urlMap
            
        
    def getHrefFromPage(self,url):
        urlList = []
        urlList = self.getElement(url,'a')
        link_list = self.getHref(urlList)
        return link_list

    def getUrl(self,url):
        re = requests.get(url)
        re.encode = "utf-8"
        soup = Bs4(re.text,'lxml')
        return soup
    
    def getElement(self,url,className):
        soup = self.getUrl(url)
        return soup.select(className)

    def getHref(self,a_list):
        link_list = []
        for x in a_list:
            link_str = x.get('href')
            print(link_str)
            if link_str:
                if len(link_str)>1:    
                    if link_str[0] == 'h':
                        link_str = link_str
                        # link_str[0] = 'h'

                    elif link_str[0] == '/':
                        if link_str[1] == '/':
                            link_str = "https:"+link_str
                    link_list.append(link_str)
            print(link_str)
        return link_list
    

def getUa(type):
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
        使用下载池控制下载负担
        taskList为任务队列，格式为
        [{
            path:xxxxxxx,
            url:xxxxxx,
        },{
            path:xxxxxxx,
            url:xxxxxx,
        }]


        --变量说明--
        thread
            -List   :线程列表
            -MaxNum :最大线程数量
        task
            -List   :任务列表
            -Key    :当前已创建下载的任务数量
            -num    :当前任务列表的长度（任务数量）
        key_Keep    :bool/False停止创建新的下载进程
        lock        :进程锁/目前还没有什么用
        pool        :下载池/目前还没有什么用
        log         :错误输出控制
        --变量说明--
        '''
        self.header = []
        self.threadList = []
        self.threadMaxNum = 10
        self.taskList = []
        self.taskKey = 0
        self.taskNum = 0
        self.key_Keep = True 
        self.lock = threading.Lock
        self.pool = []
        self.log = True

    def saveHistory(self,path):
        pass

    def pool(self,max):
        while(1):
            if self.key_Keep == False:
                self.logTag('下载已经终止')
                return False
            elif self.taskKey<=self.taskNum:
                while(len(self.threadList)<self.threadMaxNum):
                    deal = self.taskList[int(self.taskKey)]
                    self.threadList.append(_downTool_commonThread(self.downImage,(deal['url'],deal['path'])))
                    self.threadList[len(self.threadList)].start()
                    self.taskKey = self.taskKey + 1
            elif self.taskKey>self.taskNum：
                self.logTag('')
            

    def addMission(self,url,path):
        '''
        加入一个新的任务
        '''
        try:
            self.taskNum = self.taskNum + 1
            self.taskList.append({
                'path':path,
                'url':url
            })
        except:
            self.logTag("error : 添加失败 path:"+path+' url: '+url)
        else:
            self.logTag("success :"+"任务添加成功"+"path:"+path+' url: '+url)

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
                self.logTag("第"+path+"张下载好。")
                return True
        except:
            self.logTag("Error<<downImage()>>self:"+self+"-path:"+path+"-url:"+url)
            

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


class _downTool_commonThread(threading.Thread):
    def __init__(self,func,args,name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        print('线程--<<'+self.name+'>>--已启动')
        self.func(*self.args)
        print('线程--<<'+self.name+'>>--已结束')








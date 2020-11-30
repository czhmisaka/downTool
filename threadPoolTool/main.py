import threading
import os
import json
import time





class TPTool:
    def __init__(self):
        '''
        变量说明
        maxNum          : 最大线程数
        taskList        : 任务列表
        taskIndex       : 当前任务位置
        statusShow      : 信息展示列表
        statusThread    : 信息展示线程
        helper          : 守护线程
        errorlog        : 错误输出控制
        statusLog       : 线程池状态显示
        helperShow      : 守护线程输出控制
        workThreadPool  : 工作线程池
            -- index        : 线程标识
            -- thread       : thread对象
        workThreadStatus: 工作线程状态显示
            -- index        : 线程标识
            -- status       : 线程状态【我也没想好要怎么做】
        workFunc        : 工作函数
        workArgs        : 传入参数【最好搭配taskList使用】
        workReturn      : 工作结果保存【作为队列使用，按序列输出？】
        
        '''
        
        self.maxNum = 100
        self.taskList = []
        self.taskIndex = 0
        self.statusShow = []
        self.statusThread = {}
        self.helper = {}
        self.errorlog = True
        self.statusLog = True
        self.helperShow = True
        self.workThreadPool = []
        self.workThreadStatus = []
        self.workFunc = {}
        self.workArgs = {}
        self.workReturn = []
    
    def start(self):
        '''
        启动线程
        '''
        
        return 1
    
    def startHelper(self):
        '''
        线程助手
        '''
        if self.statusLog:
            self.printList(self.statusShow)
            
    def showPool(self):
        '''
        显示线程状态
        '''
        if len(self.workThreadStatus)>0:
            for x in range(len(self.workThreadStatus)):
                print(x['status'])    
    
    def log(self,p):
        '''
        错误输出显示
        '''
        if(self.errorlog):
            print(str(p))

    def printList(self,list):
        '''
        列表显示
        '''
        for x in list:
            self.log(x)




class normalThread(threading.Thread):
    '''
    公共线程类 - 通用线程
    '''
    def __init__(self,func,args,name):
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)
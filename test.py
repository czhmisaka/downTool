
import threading
import time


def loop(key):
    for i in range(key):
        print(i)
        time.sleep(1)

class test(threading.Thread):
    def __init__(self,func,args,name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        print(self.name+'号线程已经启动')
        self.func(*self.args)

lista = []
for i in range(3):
    lista.append(test(loop,[10],str(i)))
z = range(len(lista))
for i in lista:
    i.start()
from multiprocessing import Process
import os,time

class csmProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name
    def run(self):
        print("子进程--%s"%self.name)
        time.sleep(5)
        print("子进程结束")

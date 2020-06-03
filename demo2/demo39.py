

import os
import collections

def getAllFileQU(path):
    #创建一个队列
    queue = collections.deque()
    #进队
    queue.append(path)
    #队列不为空时循环
    while len(queue)!=0:
        #出队
        dirPath = queue.popleft()
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                print("目录：",fileName)
                queue.append(fileAbsPath)
            else:
                print("文件：",fileName)



getAllFileQU(r"E:\python\arm")
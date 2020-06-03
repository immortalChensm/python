import os
#使用递归遍历目录
def getFileList(path):

    filesList = os.listdir(path)
    for fileName in filesList:
        if os.path.isdir(os.path.join(path,fileName)):
            getFileList(os.path.join(path,fileName))
        else:
            print(fileName)


getFileList(r"E:\python\demo2")
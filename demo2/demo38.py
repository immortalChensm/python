import os

def getAllFileRe(path):
    #创建一个空栈
    stack = []

    #压栈
    stack.append(path)

    while len(stack)!=0:
        #出栈
        filePath = stack.pop()
        fileList = os.listdir(filePath)
        for fileName in fileList:
            fileAbsPath = os.path.join(filePath,fileName)
            if os.path.isdir(fileAbsPath):
                #判断是目录，则再次压栈
                print("目录：",fileName)
                stack.append(fileAbsPath)
            else:
                print("普通文件：",fileName)


getAllFileRe(r"E:\python\arm")
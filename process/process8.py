from multiprocessing import Pool
import time,os

def copyFile(file,toPath):

    fr = open(file,"rb")
    fw = open(toPath,"wb")
    context = fr.read()
    fw.write(context)
    fw.close()
    fr.close()

if __name__=='__main__':
    file = r"E:\python\process\file"
    toPath = r"E:\python\process\toFile"
    if not os.path.isdir(toPath):
        os.mkdir(toPath)
    start = time.time()

    for fileName in os.listdir(file):
        source = os.path.join(file,fileName)
        dest = os.path.join(toPath,fileName)

        copyFile(source,dest)




    end = time.time()
    print("耗时：%.2f"%(end-start))
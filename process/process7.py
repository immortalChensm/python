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
    pp = Pool(2)
    for fileName in os.listdir(file):
        '''source = os.path.join(file,fileName)
        dest = os.path.join(toPath,fileName)

        copyFile(source,dest)'''
        source = os.path.join(file, fileName)
        dest = os.path.join(toPath, fileName)
        pp.apply_async(copyFile,args=(source,dest))


    pp.close()
    pp.join()
    end = time.time()
    print("耗时：%.2f"%(end-start))
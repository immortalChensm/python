
import os

def worker(path):
    resPath = r"E:\python\arm"
    with open(path,"r") as f:
        while True:
            line = f.readline()
            if len(line)<=0:
                break
            emailStr = line.split("---")[0]
            resDir = emailStr.split("@")[1].split(".")[0]

            resultDirname = os.path.join(resPath, resDir)

            if not os.path.exists(resultDirname):
                os.mkdir(resultDirname)

            file = resultDirname + "/" + resDir + ".txt"
            fw = open(file, "a")
            fw.write(emailStr)
            fw.close()

worker(r"E:\python\arm\email.txt")
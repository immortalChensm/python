
path = r"E:\python\demo2\demo29.txt"

f  = open(path,"w")

#f.write("jackcsm is good man")

#f.write("jackcsm is handsome man")
#刷新缓冲区
#f.flush()
import time
while True:
    f.write("jackcsm is good man\n")
    f.flush()
    time.sleep(1)


f.close()
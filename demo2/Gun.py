class Gun(object):
    def __init__(self,blutbox):
        self.blutbox = blutbox
    def shoot(self):
        if self.blutbox.blutcount <=0:
            print("没有子弹了")
            self.blutbox.blutcount = 0
        else:
            self.blutbox.blutcount-=1
            print("还有%d发子弹"%(self.blutbox.blutcount))
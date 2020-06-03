class Person(object):
    def __init__(self,gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()
    def fillblut(self,count):
        self.gun.blutbox.blutcount = count
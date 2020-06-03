
from Father import Father
from Monther import Monther

class Child(Father,Monther):
    def __init__(self,money,faceValue):
        Father.__init__(self,money)
        Monther.__init__(self,faceValue)

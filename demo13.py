
import demo12
import os
import sys
class B(demo12.A):
    def __init__(self):
        setting = dict(
            roada=os.path.join(os.path.dirname(__file__),'/a'),
            roadb=os.path.join(os.path.dirname(__file__),'b')
        )
        demo12.A.__init__(self,setting)



b1 = B()

b1.showmsg('hello')
print(b1.setting)
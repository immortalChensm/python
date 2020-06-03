import a.jack as jack1
import b.jack as jack2
'''
包主要解决模块命名冲突的问题，包一般都默认有__init__文件，在引入包时
此文件会第一次被运行

a.jack.say()
b.jack.say()
'''

jack1.say()
jack2.say()

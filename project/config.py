import os
BASE_DIRS = os.path.dirname(__file__)

#参数
options = {
    "port":9000,
    "list":""
}

#配置
"""
tornado框架.web.Application
1、路由映射
2、参数配置
2、1 debug 设置false 为生产模式
   2 debut 设置为true为调试模式
   在此模式下有
   重启功能，代码修改或保存后自动重启，重启失败需要手动重启
   清除缓存编译的模板文件 complied_template_cache=True
   清除静态文件缓存的hash  static_hash_cache=True
   提供追踪功能
   要单独使用重启功能可以使用autlreload=True
   
   
settings给tornado.web.Application此类提供的参数是参字典传递过去，内置应该会接受并
解包【函数的参数解包]
"""
settings = {
    "debug":False,
    "static_path":os.path.join(BASE_DIRS,"static"),
    "template_path":os.path.join(BASE_DIRS,"templates")
}
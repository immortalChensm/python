import tornado.web
from views import index
import os
import config
class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            #(r"/",index.IndexHandler),
            (r"/home",index.HomeHandler),
            (r"/function",index.FunctionHandler),
            #转义功能
            (r"/transform",index.TransformHandler),

            (r"/cart",index.CartHandler),

            #StaticFileHandler 静态文件路由映射 让此StaticFileHandler去指定的目录找静态文件返回给客户端
            #注意此路由仅能写在最后面，防止它匹配了前面的路由
            #default_filename 用于只输入域名时即可访问静态文件
            (r"/(.*)$",tornado.web.StaticFileHandler,{
                "path":os.path.join(config.BASE_DIRS,"static/html"),
                "default_filename":"index.html"
            })
        ]

        super(Application,self).__init__(handler,**config.settings)
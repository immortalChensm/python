import tornado.web
import config
from views import index
from db import DB
import os
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            #(r"/",index.IndexHandler),
            (r"/index",index.IndexHandler),
            (r"/show",index.ShowHandler),
            #cookie
            (r"/pcookie",index.PcookieHandler),

            #get cookie
            (r"/getpcookie",index.GetpcookieHandler),

            #clear cookie
            (r"/clearcookie",index.ClearcookieHandler),


            #secure cookie
            (r"/scookie",index.ScookieHandler),

            #cookie 计数
            (r"/cookienum",index.CookienumHandler),

            (r"/postcookie",index.PostcookieHandler),

            #手动设置xsrf_cookie
            (r"/setXSRFcookie",index.setXSRFCookieHandler),

            #异步和同步
            (r"/async",index.AsyncHandler),

            (r"/async1",index.Async1Handler),

            (r"/sync",index.SyncHandler),

            (r"/sync1",index.Sync1Handler),

            (r"/(.*)$",tornado.web.StaticFileHandler,{
                "path":os.path.join(config.BASE_DIRS,"static/html"),
                "default_filename":"index.html"
            })
        ]
        super(Application,self).__init__(handlers,**config.settings)
        self.db = DB()
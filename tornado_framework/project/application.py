import tornado.web
import views.index as index
import config
import os
class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/jackcsm",index.JackHandler),
            (r"/function",index.FuncHandler),

            (r"/trans",index.TransHandler),

            (r"/extend",index.ExtendHandler),

            (r"/user",index.UserHandler),

            (r"/pcookie",index.PcookieHandler),
            (r"/clearpcookie",index.ClearPcookieHandler),
            (r"/scookie",index.ScookieHandler),

            (r"/gscookie",index.GscookieHandler),

            (r"/cookieNum",index.CookieNumHanlder),

            (r"/addCookieNum",index.addCookieNumHandler),

            (r"/showcookie", index.ShowCookieHandler),

            # (r"/(.*)$",tornado.web.StaticFileHandler,{
            #     "path":os.path.join(config.BASE_DIR,"static/html"),
            #     "default_filename":"index.html"
            # }),
            #login 页面
            (r"/login",index.LoginHander),

            #主页
            (r"/main",index.MainHandler),

            ("/async",index.AsyncHandler),

            (r"/(.*)$",index.AdminHanlder,{
                "path":os.path.join(config.BASE_DIR,"static/html"),
                "default_filename":"index.html"
            }),


        ]
        print(config.settings)
        super(Application,self).__init__(handler,**config.settings)
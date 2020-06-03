import tornado.web
import views.index as index
import config
class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            #(r"/",index.IndexHandler),
            #(r"/home",index.HomeHandler,{"name":"jack","age":100}),
            #tornado.web.url(r"/caasdsadasdsasm",index.CsmHandler,{"name":"b","age":"d"},name="csm"),
            #(r"/liuyifei/(\w+)/(\w+)/(\w+)",index.LiuYiFeiHandler),
            #(r"/liuyifei/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)", index.LiuYiFeiHandler),
            #(r"/zhangmanyu",index.ZhanmanyuHandler),
            #(r"/postfile",index.PostfileHanlder),
            #(r"/zhuyi",index.ZhuyiHandler),
            #(r"/upfile",index.UpfileHandler),

            #(r"/write",index.WriteHandler),

            #(r"/json1",index.JsonHandler),
            #(r"/json2",index.Json2Handler),

            #(r"/status",index.StatusHandler),

            #(r"/header",index.HeaderHandler),

            #(r"/index",index.RedirectHander),

            #(r"/error",index.ErrorHandler),

            #(r"/method",index.MethodHandler),

            (r"/jackcsm",index.JackHandler),
        ]
        print(config.settings)
        super(Application,self).__init__(handler,**config.settings)
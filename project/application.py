import tornado.web
from views import index
import config
class Application(tornado.web.Application):
    def __init__(self):
        handler = [
            (r"/",index.IndexHandler),
            (r"/home",index.HomeHandler),
            (r"/jackcsm",index.JackcsmHandler,{"sex":"Male","age":18}),
            tornado.web.url(r"/cms",index.CsmHandler,{"word3":"jack","word4":"tom"},name="csmgoodman"),
            #(r"/liyifei(\w+)/(\w+)/(\w+)",index.LiuyifeiHandler),
            (r"/liuyifei/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)",index.LiuyifeiHandler),
            (r"/zhangmanyu",index.ZhangmanyuHandler),
            (r"/postfile",index.PostfileHandler),
            (r"/zhuyi",index.ZhuyiHandler),
            (r"/linqingxia",index.UploadFileHandler),
            (r"/write",index.WriteHandler),
            (r"/json",index.JsonHandler),
            (r"/json2",index.Json2Handler),
            (r"/header",index.HeaderHandler),
            (r"/status",index.StatuscodeHandler),
            (r"/index",index.RedirectHandler),

            #错误
            (r"/iserror",index.ErrorHandler),

            #uri参数获取
            (r"/laoyoutiao/(\w+)/(\w+)/(\w+)",index.LaoyoutiaoHandler),
            #获取get参数
            (r"/laoshiji",index.LaoshijiHandler),

            #获取post参数
            (r"/semiconductor",index.SemiconductorHandler),
        ]

        super(Application,self).__init__(handler,**config.settings)
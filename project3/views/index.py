import tornado.web
from tornado.web import RequestHandler
import time
import threading

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #self.write("hello,world")
        name = "数据库"
        lists = self.application.db.table("tiny_user").find()
        self.render("index.html",lists=lists)

class PcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        #self.set_cookie("jackcsm","goodman")
        self.set_header("Set-Cookie","csm=nice;path=/")
        self.set_header("Csm","age=200")
        self.write("jackcsm is a good man")
        self.set_status(200)

class GetpcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        cookie  = self.get_cookie("csm",default="没有")
        cookie1 = self.get_cookie("jackcsm",default="不得东西")
        self.write(str(cookie)+str(cookie1))

class ClearcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        if self.get_cookie("csm"):
            self.clear_cookie("csm")
            self.write("clear cookie ok")
        else:
            self.write("cookie已经清理完毕")

class ScookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.set_secure_cookie("jackma","merchant")
        self.write("ok")
        self.get_secure_cookie("jackma")

class CookienumHandler(RequestHandler):
    def prepare(self):
        pass
    def get(self, *args, **kwargs):
        count = self.get_cookie("count", "not login")
        self.write("您是第"+str(count)+"次访问了")

class PostcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        cookie = self.get_cookie("count","not login")

        self.render("postcookie.html")
    def post(self, *args, **kwargs):

        cookie = self.get_cookie("count",None)
        if not cookie:
            cookie = 1
        else:
            cookie = int(cookie)
            cookie+=1
        self.set_cookie("count",str(cookie))
        self.redirect("cookienum")


class setXSRFCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.xsrf_token
        self.finish("设置xsrfcookie ok")

class AsyncHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write("helloa1")
        time.sleep(10)
        self.finish()

class Async1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hellob1")
        self.finish()

class SyncHandler(RequestHandler):
    def get(self, *args, **kwargs):

        def run(callbank):
            time.sleep(10)
            callbank("我睡觉了10秒钟的觉")

        threading.Thread(target=run,args=(self.finishsync,))
    def finishsync(self,data):
        self.write("给你返回数据了，老铁",data)
        self.finish()


class Sync1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("你好，世界")

class ShowHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello,laobiao")
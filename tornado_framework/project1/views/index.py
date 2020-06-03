from tornado.web import RequestHandler
import os
import config
import tornado.web
import time
import json
from tornado.httpclient import AsyncHTTPClient
from tornado.websocket import WebSocketHandler
class StudentHandler(RequestHandler):
    def Onresponse(self,response):
        if response.error:
            self.send_error(500)
        else:
            #data = json.dumps(response.body)
            data = response.body
            self.write(data)
        self.finish()
    @tornado.web.asynchronous#不关闭通信通道
    def get(self, *args, **kwargs):


        url = "http://123.56.12.53:2347/user/test"
        client = AsyncHTTPClient()
        #使用异步方式实现
        client.fetch(url,self.Onresponse)

        #self.write("ok")

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #self.write("hello")
        self.render("chat.html")


class Student2Handler(RequestHandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = "http://123.56.12.53:2347/user/test"
        #客户端
        client = AsyncHTTPClient()
        #生成器  由tornaod.gen.coroutine装饰器 负责运行该生成器【协程】后返回结果
        #生成器执行一般是next函数，会执行生成器
        res = yield client.fetch(url)
        if res.error:
            self.send_error(500)
        else:
            self.write(res.body)


class ChatHandler(WebSocketHandler):
    users = []
    def open(self, *args, **kwargs):
        self.users.append(self)
        for user in self.users:
            user.write_message(u"%s登录了"%self.request.remote_ip)
    def on_message(self, message):
        self.users.append(self)
        for user in self.users:
            user.write_message(u"%s说:%s" % (self.request.remote_ip,message))
    def on_close(self):
        self.users.remove()
        for user in self.users:
            user.write_message(u"%s退出了"%self.request.remote_ip)
    def check_origin(self, origin):
        return True


import tornado.web
import os
import config
from tornado.web import RequestHandler
class IndexHandler(RequestHandler):
    def initialize(self):
        pass
    def prepare(self):
        pass
    def set_default_headers(self):
        pass
    def write_error(self, status_code, **kwargs):
        pass
    def get(self, *args, **kwargs):
        data = dict(zip(["name", "age"], ["tony", "100"]))
        self.write(data)
    def post(self, *args, **kwargs):
        pass
    def put(self, *args, **kwargs):
        pass
    def delete(self, *args, **kwargs):
        pass
    def head(self, *args, **kwargs):
        pass
    def options(self, *args, **kwargs):
        pass
    def patch(self, *args, **kwargs):
        pass
    def on_finish(self):
        #self.write("我已经服务完成了")
        print("做一些清理工作吧")

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name":"jackcsm",
            "age":18
        }

        flag = 1

        student = [
            {
                "name":"tom",
                "age":300
            },
            {
                "name":"jack",
                "age":200
            }
        ]
        self.render("home.html",num=temp,**per,flag=flag,student=student)



class FunctionHandler(RequestHandler):
    def get(self, *args, **kwargs):

        def mySum(n1,n2):
            return n1+n2

        def get_data(p):
            return self.get_argument(p)
        self.render("market.html",mysum=mySum,get=get_data)


class TransformHandler(RequestHandler):
    def get(self, *args, **kwargs):

        str = "<h1>This is a laoyoutiao<h1>"
        self.render("trans.html",str=str)

class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("cart.html",title="购物车")
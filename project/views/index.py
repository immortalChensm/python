import tornado.web
import os
import config
from tornado.web import RequestHandler
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("csmgoodman")
        self.write("<a href=%s>点我跳转</a>"%(url))


#重定向
class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("home page")

class JackcsmHandler(RequestHandler):
    def initialize(self,sex,age):
        self.sex = sex
        self.age=age
    def get(self, *args, **kwargs):

        self.write(str(self.sex)+'is '+str(self.age))

class CsmHandler(RequestHandler):
    def initialize(self,word3,word4):
        self.name=word3
        self.age=word3
    def get(self, *args, **kwargs):
        self.write("he is good man")

class LiuyifeiHandler(RequestHandler):
    def get(self, p1,p2,p3,*args, **kwargs):
        self.write(p1+'-'+p2+'-'+p3)


class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        alist = self.get_argument('a')
        print(alist)
        self.write("zhangmanyu is a good man")

class PostfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("postfile.html")
    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        password = self.get_body_argument("passwd")
        hobbylist = self.get_body_arguments("hobby")
        print(name,password,hobbylist)
        self.write("jacksm is good man")

class ZhuyiHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.version)
        print(self.request.path)
        print(self.request.query)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write("zhuyi good female")

class UploadFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("upfile.html")
    def post(self, *args, **kwargs):
        #print(self.request.files)
        fileDict = self.request.files
        for inputName in fileDict:
            #print(inputName)
            # print(fileDict[inputName])
            fileArr = fileDict[inputName]
            for fileObj in fileArr:
                filepath = os.path.join(config.BASE_DIRS,'upfile/'+fileObj.filename)
                with open(filepath,"wb") as f:
                    f.write(fileObj.body)
            self.write("ok")

class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("jackcsm is a good man")
        self.write("jackcsm is a good man")
        self.write("jackcsm is a good man")
        self.finish()
        #self.write("csm is a good man")

class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):

        per = {
            "name":"chenssm",
            "age":18,
            "height":170
        }

        self.write(per)

import json
class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):

        per = {
            "name":"jackcsm",
            "age":18,
            "height":180
        }

        data = json.dumps(per)
        self.set_header("Content-type","application/json;charset=utf-8")
        self.set_header("jackcsm","goodman")
        self.write(data)


class HeaderHandler(RequestHandler):
    #此方法在http请求之前预设置响应头字段信息
    def set_default_headers(self):
        self.set_header("Content-Type","text/html;charset=UTF-8")
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        pass


class StatuscodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #self.set_status(404)
        self.set_status(999,"Who am i,Where are u,What are u doing")
        self.write("*************************")


class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            code = 500
            self.write("服务器内部错误")
        elif status_code== 404:
            code = 400
            self.write("您访问的页面死了")
        self.set_status(code)
    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag=='0':
            self.send_error(500)
        self.write("老表你访问的是对的")

class LaoyoutiaoHandler(RequestHandler):
    def get(self, a,b,c,*args, **kwargs):
        print(a,b,c)
        self.write("Laoyoutiao is a handsome guy")

class LaoshijiHandler(RequestHandler):
    def get(self, *args, **kwargs):
        a = self.get_query_argument("a",default="1",strip=True)
        b = self.get_query_argument("b")
        c = self.get_query_argument("c")
        print(a,b,c)
        print(args)
        print(kwargs)
        print(self.get_query_arguments("d"))
        self.write("U are Laoshiji")


class SemiconductorHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("semiconductor.html")
    def post(self, *args, **kwargs):
        print(self.get_body_arguments("hobby"))
        print(self.get_body_argument("username"))
        print(self.get_argument("username"))
        print(self.get_arguments("hobby"))
from tornado.web import RequestHandler
import os
import config
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #self.write("hi,tornado")
        #csm会找到对应的路由信息
        url = self.reverse_url("csm")
        self.write("<a href='%s'>click me</a>"%(url))

class HomeHandler(RequestHandler):
    def initialize(self,name,age):
        self.name = name
        self.age  = age
    def get(self, *args, **kwargs):
        self.write("your name is %s and your age is %s"%(self.name,self.age))

class CsmHandler(RequestHandler):
    def initialize(self,name,age):
        self.a = name
        self.b = age
    def get(self, *args, **kwargs):
        self.write("vari1 is %s and onther is %s"%(self.a,self.b))

class LiuYiFeiHandler(RequestHandler):
    def get(self, p1,p2,p3,*args, **kwargs):
        print(p1,p2,p3)
        print("liu is beauty girl")
        self.write("she is nice girl")

class ZhanmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.get_arguments("a"))
        a = self.get_query_argument("a",default=100,strip=False)
        b = self.get_query_argument("b",default=200,strip=True)
        c = self.get_query_argument("c")
        print(a,b,c)
        self.write("she is so beauty")
class PostfileHanlder(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("postcookie.html")
    def post(self, *args, **kwargs):
        #user = self.get_body_argument("user")
        #pwd  = self.get_body_argument("pwd")
        #hobby = self.get_body_arguments("hobby")

        user = self.get_argument("user")
        pwd = self.get_argument("pwd")
        hobby = self.get_arguments("hobby")
        print(user,pwd,hobby)
        self.write("i am a good teacher")

class ZhuyiHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.files)
        print(self.request.host)
        print(self.request.remote_ip)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.version)
        self.write("hi")

class UpfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("upfile.html")
    def post(self, *args, **kwargs):
        #print(self.request.files)
        files = self.request.files
        for fileArr in files:
            fileS = files[fileArr]
            for fileObj in fileS:
                link = os.path.join(config.BASE_DIR,"upfile/"+fileObj.filename)
                with open(link,"wb") as f:
                    f.write(fileObj.body)
                f.close()

        self.write("上传ok")

class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('a')
        self.write('b')
        self.write('c')
        self.finish()


import json
class JsonHandler(RequestHandler):
    def get(self, *args, **kwargs):

        data = {
            "name":"tony",
            "age":19
        }
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.write(json.dumps(data))

class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        data = {
            "name":"jack",
            "age":18
        }

        self.write(data)


class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type","text/html;charset=UTF-8")
        self.set_header("server","python3")
    def get(self, *args, **kwargs):
        data = {"a":"b"}
        self.set_header("language","python3")
        self.write(data)



class StatusHandler(RequestHandler):
    def get(self, *args, **kwargs):

        #self.set_status(404)
        self.set_status(600,'dont know what erros')
        self.write("doing")

class RedirectHander(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")

class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code==500:
            self.write("500啦")
        elif status_code==404:
            self.write("404啦")
        self.set_status(status_code)
    def get(self, *args, **kwargs):
        error = self.get_query_argument("flag")
        print(type(error))
        if error=='1':
            self.send_error(404)
        else:
            self.write("ok")

class MethodHandler(RequestHandler):
    def initialize(self):
        pass
    def prepare(self):
        self.write("prepare")
    def write_error(self, status_code, **kwargs):
        pass
    def get(self, *args, **kwargs):
        self.write("method")
    def post(self, *args, **kwargs):
        pass
    def put(self, *args, **kwargs):
        pass
    def delete(self, *args, **kwargs):
        pass
    def options(self, *args, **kwargs):
        pass

    def set_default_headers(self):
        pass
    def on_finish(self):
        print("finish")



class JackHandler(RequestHandler):
    def get(self, *args, **kwargs):
        num = 100000000000000000

        person = {
            "name":"jack",
            "age":16
        }
        flag = 28

        student = [
            {"name":"张飞","age":30},
            {"name":"刘备","age":34}
        ]
        self.render("jack.html",num=num,person=person,flag=flag,student=student)
from tornado.web import RequestHandler
import os
import config
import tornado.web
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

class FuncHandler(RequestHandler):
    def get(self, *args, **kwargs):
        n1 = int(self.get_query_argument("n1"))
        n2 = int(self.get_query_argument("n2"))
        def myself(n1,n2):
            return n1+n2
        result = myself(n1,n2)
        self.render("func.html",result=result)

class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h4>jackcsm is famous boss</h4>"
        self.render("trans.html",str=str)

class ExtendHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.render("cart.html",title='cart')

class UserHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.render("user.html",title='user')

class PcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.set_cookie("jack","800000000000000")
        print(self.get_cookie("jack"))
        self.write('cookie')

class ClearPcookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        print(self.get_cookie("jack"))

        import time
        time.sleep(2)
        #self.clear_cookie("jack")

        self.clear_all_cookies()
        self.write("清除了cookie")

class ScookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        #5031a58f4069cb7fc8d10d1469092819fe49de1f241483753f3dde3088b1b524
        self.set_secure_cookie("girl","liuyifei")
        self.write("ok")

class GscookieHandler(RequestHandler):
    def get(self, *args, **kwargs):

        cookie = self.get_secure_cookie("girl")
        print(cookie)
        self.write(cookie)

class CookieNumHanlder(RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie("count", "nologin")
        self.render("cookieNum.html",count=count)

class addCookieNumHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("addcookie.html")
    def post(self, *args, **kwargs):
        count = self.get_cookie("count")

        if not count:
            count = 1
        else:
            count = int(count)
            count += 1

        self.set_cookie("count", str(count))
        #self.redirect("/cookieNum")
        self.write("请求成功")

class ShowCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("postcookie.html",count=self.get_cookie("count"))
    def post(self, *args, **kwargs):
        print(self.get_body_argument("user"))
        self.finish("ok")

class AdminHanlder(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(AdminHanlder,self).__init__(*args,**kwargs);
        self.xsrf_token

class MainHandler(RequestHandler):
    #获取当前的登录用户  返回True时执行下一个请求
    def get_current_user(self):
        flag = self.get_argument("flag",None)
        return flag
        #return False#返回假则重定向到login_url的配置值
    @tornado.web.authenticated#python装饰器  功能将此函数当作参数传递给tornado处理后再返回结果
    def get(self, *args, **kwargs):
        self.render("main.html")

class LoginHander(RequestHandler):
    def post(self, *args, **kwargs):

        name = self.get_argument("user")
        pwd = self.get_argument("pwd")
        if name=='1' and pwd == '1':
            next = self.get_argument("next","/")
            self.redirect(next+"?flag=logined")
        else:
            next = self.get_argument("next","/login")
            self.redirect(next)

    def get(self, *args, **kwargs):
        self.render("login.html")

class AsyncHandler(RequestHandler):
    def post(self, *args, **kwargs):
        self.write("异步")
    def get(self, *args, **kwargs):
        self.render("async.html")
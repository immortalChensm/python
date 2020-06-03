#coding=utf-8
import tornado.web
import tornado.ioloop
from gpiozero import LED

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("欢迎访问LED控制面板")


class LedHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request)
        html = """
        <html>
            <title>LED控制面板</title>
            <body>
                <button data="1">1号房间的灯</button>
                <div class="status"></div>
                <script type="text/javascript">
                   
                   window.onload = function(e){
                        
                        document.getElementsByTagName("button")[0].onclick = function(){
                            var that = this;
                            ajax({
                                url:"http://192.168.1.8:9080/lamp",
                                data:{
                                    "on":that.getAttribute("data"),
                                },
                                success:function(xhr){
                                    alert(xhr.responseText);
                                    if(that.getAttribute("data")==1){
                                        that.setAttribute("data",2);
                                    }else{
                                        that.setAttribute("data",1);
                                    }
                                    
                                },
                                error:function(xhr){
                                    alert(xhr.statusText);
                                },
                            });
                        };
                        
                        function ajax(obj){
                            xhr = new XMLHttpRequest();
                        
                            xhr.onreadystatechange = function(){
                            if(xhr.readyState==4){
                                if(xhr.status==200){
                                    //document.querySelector(".status").innerHTML=xhr.responseText;
                                    //alert(xhr.responseText);
                                    obj.success(xhr);
                                }else{
                                    //console.error(xhr.statusText);
                                    obj.error(xhr);
                                }
                            }
                            };
                        
                            xhr.onerror = obj.error(xhr);
                            url = obj.url;
                        
                            //xhr.open("GET",url,true);
                            //xhr.send(null);
                            var formData = new FormData();
                            formData.append("name","jack");
                            formData.append("age",100);
                        
                            xhr.open("POST",url,true);
                            //xhr.setRequestHeader("Content-type","application/x-www-form-urlencode");
                            xhr.setRequestHeader("Content-type","application/json");
                            var data = {
                                'name':'jack',
                                'age':1000
                            }
                            xhr.send(JSON.stringify(obj.data));
                        }
                        
                   }
                </script>
            </body>
        </html>
        """
        self.write(html)

class LampHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("lamp view")
    def post(self, *args, **kwargs):
        #print(self.request.body)
        #print(eval(self.request.body))
        request = eval(self.request.body)
        #print(request['on'])
        led = LED(27)
        while True:
            if request['on'] == '1':
                led.on()
                self.write("灯开了")
            else:
                led.off()
                self.write("灯关了")



if __name__=='__main__':

    app = tornado.web.Application([
        (r"/",IndexHandler),
        (r"/led",LedHandler),
        (r"/lamp",LampHandler)
    ])

    app.listen(9080)
    tornado.ioloop.IOLoop.current().start()


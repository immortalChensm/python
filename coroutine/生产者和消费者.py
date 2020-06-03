'''
python协程采用generator生成器生成
yield 产量 生产
当生成器对象调用send方法时【产生一个中断请求，此时生成器响应中断请求，执行yield data之后，响应并返回】
此时再调用send方法时，再次完成中断的请求和中断响应

原理类似cpu中断
'''
def product(c):
    c.send(None)
    for i in range(5):
        print("生产者生产了%s"%i)
        r = c.send(str(i))
        print("消费者返回了%s"%r)
    c.close()
def consumer():

    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了%s"%n)
        data = 200

c = consumer()
product(c)
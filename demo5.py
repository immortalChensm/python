import requests
from gpiozero import LED

url = "http://www.itkucode.com/demo/wechat/Home/Index/getLedstate"
led = LED(27)
while True:
    result = requests.get(url).json()

    if result['led'] == '1':
        led.on()

    elif result['led'] == '2':
        led.off()

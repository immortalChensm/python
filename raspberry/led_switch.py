from gpiozero import LED,Button
import time
led = LED(17)
button = Button(2)

while True:
    button.wait_for_press()
    led.toggle()
    time.sleep(3)
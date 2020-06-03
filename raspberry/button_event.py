from gpiozero import LED,Button
from signal import pause
import time
led = LED(17)
button = Button(2)

button.when_pressed = led.on
print("led is on")
button.when_released = led.off
print("led is off")

pause()
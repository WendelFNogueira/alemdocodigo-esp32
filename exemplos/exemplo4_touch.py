from machine import Pin, TouchPad
import time

touch = TouchPad(Pin(4))  # GPIO4
led = Pin(2, Pin.OUT)

while True:
    valor = touch.read()
    print("Valor do sensor:", valor)

    if valor < 400:  # Limite para detectar toque
        led.value(1)
    else:
        led.value(0)

    time.sleep(0.2)

# Exemplo 1: Piscar LED no ESP32
# Este código acende e apaga um LED conectado ao pino 2 (onboard) em intervalos de 1 segundo.
# Demonstra o uso básico de GPIO digital.

import machine
import time

led = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)  # Liga o LED
    time.sleep(1)
    led.value(0)  # Desliga o LED
    time.sleep(1)

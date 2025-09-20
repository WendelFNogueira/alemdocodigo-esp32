# Exemplo 3: Controle de brilho com PWM
# Este código usa PWM para aumentar e diminuir o brilho de um LED gradualmente.
# Mostra como controlar intensidade de sinais analógicos simulados.

import machine
import time

led = machine.PWM(machine.Pin(2))
led.freq(1000)

while True:
    for duty in range(0, 1024, 10):  # Aumenta brilho
        led.duty(duty)
        time.sleep(0.01)
    for duty in range(1023, -1, -10):  # Diminui brilho
        led.duty(duty)
        time.sleep(0.01)

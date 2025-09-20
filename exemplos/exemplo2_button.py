# Exemplo 2: Ler botão no ESP32
# Este código lê o estado de um botão conectado ao pino 15.
# Se o botão for pressionado, acende o LED interno no pino 2.

import machine

led = machine.Pin(2, machine.Pin.OUT)
botao = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if botao.value() == 1:
        led.value(1)  # Liga LED
    else:
        led.value(0)  # Desliga LED

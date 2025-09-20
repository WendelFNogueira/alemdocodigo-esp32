# Exemplo 5: Conectar o ESP32 ao Wi-Fi
# Este código conecta o ESP32 a uma rede Wi-Fi usando SSID e senha definidos.
# Depois exibe o endereço IP atribuído.

import network
import time

ssid = "NOME_DA_REDE"
password = "SENHA_DA_REDE"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Conectando ao Wi-Fi...")
while not wifi.isconnected():
    time.sleep(1)

print("Conectado! IP:", wifi.ifconfig()[0])

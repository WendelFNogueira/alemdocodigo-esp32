# Exemplo 6: Servidor Web simples
# Este código cria um servidor HTTP no ESP32.
# Quando acessado pelo navegador, retorna uma página com "Olá, IoT!".

import network
import socket
import time

# Configuração do Wi-Fi
ssid = "NOME_DA_REDE"
password = "SENHA_DA_REDE"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Conectando ao Wi-Fi...")
while not wifi.isconnected():
    time.sleep(1)

print("Conectado! IP:", wifi.ifconfig()[0])

# Servidor socket
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Servidor iniciado em http://%s" % wifi.ifconfig()[0])

while True:
    cl, addr = s.accept()
    print("Cliente conectado:", addr)
    cl_file = cl.makefile("rwb", 0)
    cl_file.readline()
    resposta = """\
HTTP/1.1 200 OK

<html>
  <h1>Olá, IoT!</h1>
  <p>Servidor ESP32 rodando em MicroPython 🚀</p>
</html>
"""
    cl.send(resposta)
    cl.close()

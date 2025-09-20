# Além do Código - ESP32 🛰️

Repositório oficial do projeto educacional **Além do Código** para introdução ao **ESP32** utilizando **MicroPython**.  
O objetivo é fornecer um espaço de aprendizado acessível para estudantes e entusiastas de tecnologia que desejam explorar IoT, programação embarcada e prototipagem com ESP32.

---

## 📌 Objetivos
- Aprender a programar o **ESP32** com **MicroPython**.
- Explorar sensores, atuadores e módulos em projetos práticos.
- Criar uma base de estudos que pode ser usada tanto em sala de aula quanto por autodidatas.
- Facilitar o acesso ao conhecimento com tutoriais, exemplos e recomendações de hardware acessível.

---

## 🛠️ Pré-requisitos

### 1. Instalar o Thonny IDE
Baixe o Thonny em: [https://thonny.org](https://thonny.org)  
- Execute o instalador e siga as instruções padrão.  
- Durante a instalação, selecione a opção para incluir o **Python 3.10+** (se solicitado).  

### 2. Instalar o driver do ESP32 (Windows)
O Windows precisa do driver **Silicon Labs CP210x** para reconhecer o ESP32.  
Baixe em: [https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)

Após a instalação, conecte seu ESP32 via cabo USB e confirme no **Gerenciador de Dispositivos** que ele aparece em **Portas COM**.

### 3. Configurar o Thonny para ESP32
- Abra o **Thonny**  
- Vá em: `Ferramentas > Opções > Interpretador`  
- Escolha: **MicroPython (ESP32)**  
- Em **Porta**, selecione a porta COM do seu ESP32  

Pronto! Você já pode enviar seus primeiros códigos.

---

## 📂 Estrutura do repositório
```

alemdocodigo-esp32/
│
├── exemplos/          # Códigos de exemplo em MicroPython
├── projetos/          # Projetos práticos guiados
├── docs/              # Tutoriais, guias e referências
└── README.md          # Este arquivo

```


---

## 🔌 Componentes básicos utilizados

- ESP32 DevKit v1
- Protoboard
- Jumpers (fios de conexão)
- LEDs e resistores
- Micro servo motor SG90
- Sensor touch TTP223B
- Tela OLED (I2C)
- Sensores diversos (kit inicial)

---

## 🔌 Componentes que tenho para testes e prototipação

#### 🔧 Placas Principais

1. **ESP32 Development Board (1x)**

   * Wi-Fi + Bluetooth embutidos.
   * Exemplo: controle remoto por celular, envio de dados para nuvem.

2. **ESP32 DevKit DOIT (1x)**

   * Placa extra de testes.

3. **ESP32-CAM + câmera OV2640 (1x)**

   * Transmissão de vídeo e captura de imagens.
   * Exemplo: vigilância, reconhecimento facial.

---

#### 📺 Displays e Interfaces

4. **Display OLED 0.96” (1x)**

   * Exibe dados como temperatura ou mensagens.

---

#### 🛠️ Montagem

5. **Protoboard 830 pontos (1x)**
6. **Protoboard 400 pontos (1x)**
7. **Jumpers (65x)**
8. **Resistores (30x)**
9. **Botões Push Button (6x)**
10. **LEDs (vermelhos, amarelos, verdes e RGB)**

---

#### 🌡️ Sensores

11. **Sensor Infravermelho de Obstáculos (1x)** – carros que evitam colisão.
12. **Sensor LDR (1x)** – acende luz no escuro.
13. **Sensor DHT11 (1x)** – mede temperatura e umidade.
14. **Sensor PIR HC-SR501 (1x)** – detecta movimento.
15. **Potenciômetro 10K (1x)** – controle analógico.
16. **Sensor Ultrassônico HC-SR04 (1x)** – mede distância.
17. **MPU6050 (1x)** – acelerômetro + giroscópio.
18. **Kit RFID RC522 (1x)** – leitura de cartões/tag por aproximação.

---

#### 🔊 Atores (Saídas)

19. **Buzzers Ativo e Passivo (1x cada)** – sons e alarmes.
20. **Módulo Relé 2 canais (1x)** – liga/desliga cargas externas.
21. **Shield L293D (1x)** – ponte H para motores DC.

---

#### 💾 Armazenamento e Alimentação

22. **Módulo Leitor de Cartão TF (1x)** – leitura/escrita em microSD.
23. **Módulo de Alimentação MB102 (1x)** – fonte 3.3V/5V para protoboard.

---

#### 🤖 Robótica

24–36. **Motores DC, engrenagens, rodas, receptor de carrinho, conectores, chave liga/desliga e peças diversas** → base para projetos de robótica.

---

#### 💡 Exemplos de Projetos Possíveis

* 🚗 **Carro autônomo** com sensor ultrassônico + ponte H.
* 🖐 **Carro controlado por gestos** com MPU6050.
* 🏠 **Casa inteligente**: luz automática (LDR), irrigação de plantas (DHT11 + relé + bomba).
* 📷 **Monitoramento com ESP32-CAM**.
* 🔐 **Controle de acesso com RFID**.
* 🌡 **Estação climática IoT** com envio de dados para nuvem.
* 🚦 **Semáforo inteligente** em maquete.

---

📌 **Dica**: Para cada componente, pesquise no YouTube usando:
`ESP32 [nome do componente] MicroPython português`

---

## 🛒 Recomendações de compra

Para quem deseja montar seu próprio kit de estudos:  

- [ESP32 (menos de R$50)](https://s.shopee.com.br/gGpsDBZb7)  
- [Kit básico ESP32 com módulos, resistores, tela OLED, sensores e etc.](https://s.shopee.com.br/2LP3rWY1VM)  
- [Micro servo motor SG90](https://s.shopee.com.br/3fuRS8gVTT)  
- [Sensor touch TTP223B](https://s.shopee.com.br/1VpwsPZUaz)  

---

## 🤝 Contribuição
Quer contribuir?  
- Faça um **fork** do repositório  
- Crie uma **branch** para sua modificação  
- Envie um **pull request**  

Sugestões de melhorias, exemplos e novos projetos são bem-vindos!

---

## 📜 Licença
Este projeto é distribuído sob a licença **MIT**.  
Você pode usá-lo livremente para fins pessoais, educacionais e comerciais.

---

## ✨ Autor
**Wendel Nogueira**  
Desenvolvedor Backend Java Sênior na GFT Brasil | Certificado AWS | Apaixonado por ensinar e compartilhar conhecimento.  
[LinkedIn](https://www.linkedin.com/in/wendelfnogueira)

from machine import Pin
from utime import sleep

print("Hello World!")

ledVerde = Pin(15, Pin.OUT)
ledAmarelo = Pin(16, Pin.OUT)
ledVermelho = Pin(17, Pin.OUT)

while True:
    ledVerde.on()
    print("Led Verde ON!")
    sleep(20)
    ledVerde.off()
    print("Led Verde OFF")
    sleep(0.5)

    ledAmarelo.on()
    print("Led Amarelo ON!")
    sleep(10)
    ledAmarelo.off()
    print("Led Amarelo OFF")
    sleep(0.5)

    ledVermelho.on()
    print("Led ON!")
    sleep(7)
    ledVermelho.off()
    print("Led OFF")
    sleep(0.5)
    
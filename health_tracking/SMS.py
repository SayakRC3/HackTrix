import serial
import os, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

port.write(b'AT\r')
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write(b"AT+CMGF=1\r")
print("Text Mode Enabled…")
time.sleep(3)
port.write(b'AT+CMGS="9875487995"\r')
msg = "hackathon jitenge"
print("sending message….")
time.sleep(3)
port.reset_output_buffer()
time.sleep(1)
port.write(str.encode(msg+chr(26)))
time.sleep(3)
print("message sent…")


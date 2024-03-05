import serial
import os, time
import RPi.GPIO as GPIO
import time
import max30100

mx30 = max30100.MAX30100()
mx30.enable_spo2()
consecutive_abnormalities = 0
GPIO.setmode(GPIO.BOARD)
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

port.write(b'AT\r')
rcv = port.read(10)
print(rcv)
time.sleep(1)

while 1:
    mx30.read_sensor()

    mx30.ir, mx30.red
    
    hb = int(mx30.ir / 100)-100
    spo2 = int(mx30.red / 100)
    
    if mx30.ir != mx30.buffer_ir :
        print("Pulse:",hb);
        
    if hb < 40 or hb > 110:
        consecutive_abnormalities += 1
    else:
        consecutive_abnormalities = 0  # Reset counter if the condition is not met

    if consecutive_abnormalities >= 5:
        print("Abnormality detected")
        port.write(b"AT+CMGF=1\r")
        print("Text Mode Enabled…")
        time.sleep(3)
        port.write(b'AT+CMGS="9875487995"\r')
        msg = "Abnormality detected"
        print("sending message….")
        time.sleep(3)
        port.reset_output_buffer()
        time.sleep(1)
        port.write(str.encode(msg+chr(26)))
        time.sleep(3)
        print("message sent…")
    else:
        print("You are ok!!!")
        

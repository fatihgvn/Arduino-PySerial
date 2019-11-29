#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial

# port ismi linux a göre yazıldı
# eğer windows kullanılıyorsa port ismi COM3 gibi bir ifade olucaktır

ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600) 
 
while True:
    try:
        line = ser.readline().decode("utf-8")[:-2]
        print(line)
    except KeyboardInterrupt:
        break
 
ser.close()
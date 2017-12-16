#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:40:47 2017

@author: james
"""

import sys
import time
import pigpio

GPIO=21
delay_time=0.5
repeat_number=10

pi = pigpio.pi("100.100.100.5")

pi.set_mode(GPIO, pigpio.OUTPUT)


for count in range(repeat_number):
    print(count)
    pi.write(GPIO,0)
    time.sleep(delay_time)
    pi.write(GPIO,1)
    time.sleep(delay_time)
    

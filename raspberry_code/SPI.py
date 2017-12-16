#!/usr/bin/env python

# 2014-08-26 PCF8591.py

import matplotlib.pyplot as plt
import numpy as np
import pigpio
import time

data_length=10000;
fig=plt.figure(1)
Z=np.zeros([data_length,3]);

# Address of accelerometer
ADXL312Z=0x53

# Connect to raspberry pi on network
pi = pigpio.pi("100.100.100.5") # Connect to local Pi.

handle = pi.spi_open(0,10000000,3)


# Check device ID is correct
(no,data_temp)=pi.spi_xfer(handle,[0b10000000,0])
devID=data_temp[1]
if devID == 0b11100101:
    print("Device is correct: {:b}".format(devID))
else:
    print("Device not correct: {:b}".format(devID))
    
# Set bitrate
bt_rate = {"3200" :0b1111,"1600" :0b1110,"800" :0b1101,"400" :0b1100,
           "200" :0b1011,"100" :0b1010,"50" :0b1001,"25" :0b1000,
           "12.5" :0b0111,"6.25" :0b0110}

pi.spi_xfer(handle,[0x2c,bt_rate["50"]])

# Set device to measurement mode
pi.spi_xfer(handle,[0x2D,0b00001011])

# Set device data format (left justified, +-6g, 10bit mode)
pi.spi_xfer(handle,[0x31,0b00001110])

# Set FIFO settings (Streaming, INT1, 32 in FIFO to trigger watermark)
pi.spi_xfer(handle,[0x38,0b10000001])

#Zero device
(no,data_temp)=pi.spi_xfer(handle,[0b11110010,0,0,0,0,0,0,0,0])

bird=[0,0,0]
for james in range(0,data_length):
    (no,data_temp)=pi.spi_xfer(handle,[0b11110010,0,0,0,0,0,0,0,0])
    for count in range(0,3):
        Z[james,count]=(((data_temp[(count*2)+2]<<8)+data_temp[(count*2)+1])>>4);


plt.plot(Z)
plt.show()

    
#(no,data)=pi.spi_xfer(handle,[0x2c+0x80,0])
#print( bin(data[1]))
#pi.i2c_write_byte_data(handle,0x2C,bt_rate["3200"])





#data=pi.spi_read(handle,57)






#
#
#
#
#
## Open I2C connection, return handle
#handle = pi.i2c_open(1, ADXL312Z)
#
## Check device ID is correct
#devID=pi.i2c_read_byte_data(handle,0x00)
#if devID == 0b11100101:
#    print("Device is correct: {:b}".format(devID))
#else:
#    print("Device not correct: {:b}".format(devID))
#    
## Set bitrate
#bt_rate = {"3200" :0b1111,"1600" :0b1110,"800" :0b1101,"400" :0b1100,
#           "200" :0b1011,"100" :0b1010,"50" :0b1001,"25" :0b1000,
#           "12.5" :0b0111,"6.25" :0b0110,}
#pi.i2c_write_byte_data(handle,0x2C,bt_rate["3200"])
#
## Set device to measurement mode
#pi.i2c_write_byte_data(handle,0x2D,0b00001011)
#
## Set device data format (left justified, +-1.5g, 10bit mode)
#pi.i2c_write_byte_data(handle,0x31,0b00000100)
#
## Set FIFO settings (Streaming, INT1, 32 in FIFO to trigger watermark)
#pi.i2c_write_byte_data(handle,0x38,0b10000001)
#
#no_bts=1
#
#for count in range(100):
#
#    (a,b)=(pi.i2c_read_i2c_block_data(handle,0x32,no_bts))
#    (a1,b1)=(pi.i2c_read_i2c_block_data(handle,0x33,no_bts))
#    (a2,b2)=(pi.i2c_read_i2c_block_data(handle,0x34,no_bts))
#    (a3,b3)=(pi.i2c_read_i2c_block_data(handle,0x35,no_bts))
#    (a4,b4)=(pi.i2c_read_i2c_block_data(handle,0x36,no_bts))
#    (a5,b5)=(pi.i2c_read_i2c_block_data(handle,0x37,no_bts))
#
##   
    
#temp=pi.i2c_read_byte_data(handle,0x33)
#
#pi.i2c_write_byte_data(handle,0x2C,0b00001010)
#
#pi.i2c_write_byte_data(handle,0x2D,0b00100)
#
#pi.i2c_write_byte_data(handle,0x31,0b00001100)
#
#pi.i2c_write_byte_data(handle,0x38,0b10011111)
#
#temp2=pi.i2c_read_byte_data(handle,0x39)
#
#print(temp2)




#stdscr = curses.initscr()
#
#curses.noecho()
#curses.cbreak()

#aout = 0
#
#stdscr.addstr(10, 0, "Brightness")
#stdscr.addstr(12, 0, "Temperature")
#stdscr.addstr(14, 0, "AOUT->AIN2")
#stdscr.addstr(16, 0, "Resistor")
#
#stdscr.nodelay(1)
#
#try:
#   while True:
#
#      for a in range(0,4):
#         aout = aout + 1
#         pi.i2c_write_byte_data(handle, 0x40 | ((a+1) & 0x03), aout&0xFF)
#         v = pi.i2c_read_byte(handle)
#         hashes = v / 4
#         spaces = 64 - hashes
#         stdscr.addstr(10+a*2, 12, str(v) + ' ')
#         stdscr.addstr(10+a*2, 16, '#' * hashes + ' ' * spaces )
#
#      stdscr.refresh()
#      time.sleep(0.04)
#
#      c = stdscr.getch()
#
#      if c != curses.ERR:
#         break
#
#except:
#   pass
#
#curses.nocbreak()
#curses.echo()
#curses.endwin()
#
pi.spi_close(handle)
#
pi.stop()


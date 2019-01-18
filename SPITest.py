import spidev
from time import sleep
import sys

spi = spidev.SpiDev()
spi.open(0, 0) #SPI bus 0, device 0
spi.max_speed_hz = 1000000 #max speed of 1MHz
value = 0

def charToInt(x):
    return ord(x)

while True:
    data_list = [ [],[],[],[] ]
#    raw = ['S', 'D', 'A', 'V']    
#    data_out = []
#    data_out = [charToInt(item) for item in raw]  #convert the characters to numbers
    data_list[0] = [ord('S'), 50, 100, 150, 200, 0] #test of Speed setting
    data_list[1] = [ord('D'), 10, 2, 20, 3, 30, 4, 40, 5, 0] #test of distance setting
    data_list[2] = [ord('A'), 100, 0] #test of acceleration setting
    data_list[3] = [ord('V'), 9, 0]
    for data_out in data_list:
        r = spi.xfer(data_out)
        print('Sent '+ str(data_out))
        print('Received '+ str(r))
        sleep(1)

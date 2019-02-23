import spidev
from time import sleep
import sys


class motorController():

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0) #SPI bus 0, device 0
        self.spi.max_speed_hz = 1000000 #max speed of 1MHz

    def setMotorSpeed(self, speed1,speed2, speed3, speed4):
        data_out = [ord('S'), speed1,speed2,speed3,speed4, 255] #test of Speed setting
        recv=self.send(data_out)
        return recv

	       
    def setDistance(self, distance1,speed1,distance2, speed2, distance3, speed3, distance4, speed4):
        data_out = [ord('D'), distance1, speed1, distance2, speed2,distance3, speed3, distance4, speed4, 255]
        recv=self.send(data_out)
        return recv


    def setMaxAccel(self, maxAccel):
        data_out = [ord('A'), maxAccel,255]
        recv=self.send(data_out)
        return recv


    def getADC(self,n):
        data_out = [ord('V'), n, 255]
        recv=self.send(data_out)
        return recv
	        

    def send(self, data_out):
        r = self.spi.xfer(data_out)
#        print('Sent '+ str(data_out))
        #print('Received '+ str(r))
        return r

if __name__ =="__main__":
    myMC=motorController()
    r=myMC.setMotorSpeed(5,5,5,5)
#    print('Received', str(r))
    r=myMC.setDistance(1,2,3,4,5,6,7,8)
 #   print('Received', str(r))
    r=myMC.setMaxAccel(1)
  #  print('Received', str(r))
    r=myMC.getADC(1)
    print('Received', str(r))

import spidev
from time import sleep
import sys
import ctypes


class motorController():

    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0) #SPI bus 0, device 0
        self.spi.max_speed_hz = 10000 #max speed of 1MHz, practical limit is 10kHz

    def __del__(self):
        self.spi.close()

    def setMotorSpeed(self, speed1,speed2, speed3, speed4): #set the motor speed from -100 to + 100
        speed1=speed1+128
        speed2=speed2+128
        speed3=speed3+128
        speed4=speed4+128
        data_out = [ord('S'), speed1,speed2,speed3,speed4, 255] #test of Speed setting
        recv=self.send(data_out)
        return recv

	       
    def setDistance(self, distance1, distance2, distance3, distance4, speed1, speed2, speed3, speed4): #set the motor distance as a max speed. all in range of -100 to 100
        speed1=speed1+128
        speed2=speed2+128
        speed3=speed3+128
        speed4=speed4+128
        distance1=distance1+128
        distance2=distance2+128
        distance3=distance3+128
        distance4=distance4+128
        data_out = [ord('D'), distance1, distance2, distance3, distance4, speed1, speed2, speed3, speed4, 255]
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
        print('Sent '+ str(data_out))
        #print('Received '+ str(r))
#        sleep(1)
        return r

if __name__ =="__main__":
    myMC=motorController()
    r=myMC.setMotorSpeed(0,0,0,0)
    print('Received', str(r))
#    r=myMC.setDistance(1,2,3,4,5,6,7,8)
#    print('Received', str(r))
#    r=myMC.setMaxAccel(100)
#    print('Received', str(r))
    r=myMC.getADC(5)
    print('Received', str(r))
#    motorController.spi.close()

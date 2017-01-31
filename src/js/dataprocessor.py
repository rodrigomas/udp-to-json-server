#!/usr/bin/env python3
'''
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
'''
from abc import ABCMeta, abstractmethod
from _pyio import __metaclass__
import struct
import logging
import base64
import array

SOH = 0x01
EOT = 0x04

class DataProcessor(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, params):
        pass
    
    @abstractmethod
    def process(self, data, address):
        pass
        

class F1DataProcessor(DataProcessor):
    def __init__(self):
        self.info = None
        self.log = False        
        
    def enableLog(self):
        self.log = True
    
    def disableLog(self):
        self.log = False
        
    def getInfo(self):
        return self.info    
        
    def process(self, data, info, address):
         
        print('Processing New Data')
        
        if(self.log == True):
            #logging.info(data)
            if(address != None):
                logging.info(address)
                
            logging.info(base64.b64encode(array.array('B',map(ord,data))))
            
        self.info = info              
        
        try:             
                    
            for i in range(0, len(data)):
                if(ord(data[i]) == SOH):                   
                    if (ord(data[i+1]) == ord('M')): #M 0x4D
                        print('M Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])) & 0x00FF
                         
                        checksum = ord(data[i+4])
                         
                        if(ssum != checksum and ord(data[i + 5]) != EOT):
                            continue                         
                            
                        self.info.setMentalDir(data[i+2])
                        self.info.setMentalIntensity(ord(data[i+3]) - ord('0'))
                         
                    elif (ord(data[i+1]) == ord('R')): #R 0x52
                        print('R Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3]) + ord(data[i+4])) & 0x00FF
                        
                        checksum = ord(data[i+5]) 
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                         
                        self.info.setANNDir(data[i+2])
                        self.info.setANNAngle((ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0'))
                    elif (ord(data[i+1]) == ord('A')): #A
                        print('A Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')                    
                        
                        self.info.setAcceleration(val)                        
                    elif (ord(data[i+1]) == ord('V')): #V
                        print('V Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setSpeed(val)                                                 
                    elif (ord(data[i+1]) == ord('T')): #T
                        print('T Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setTemperature(val)
                    elif (ord(data[i+1]) == ord('D')): #D
                        print('D Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setDirection(val)
                    elif (ord(data[i+1]) == ord('L')): #L
                        print('L Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setLimit(val)                        
                    elif (ord(data[i+1]) == ord('B')): #B
                        print('B Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setBPM(val)
                        
                    elif (ord(data[i+1]) == ord('E')): #E
                        print('E Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setTempBody01(val)      
                        
                    elif (ord(data[i+1]) == ord('F')): #F
                        print('F Message')
                        ssum = (ord(data[i+1]) + ord(data[i+2]) + ord(data[i+3])  + ord(data[i+4])) & 0x00FF
                         
                        checksum = ord(data[i+5])
                         
                        if(ssum != checksum and ord(data[i + 6]) != EOT):
                            continue
                        
                        val = (ord(data[i+2]) - ord('0')) * 100 + (ord(data[i+3]) - ord('0')) * 10 + ord(data[i+4]) - ord('0')
                        
                        self.info.setTempBody02(val)
                          
                    elif (ord(data[i+1]) == ord('G')): #G
                        print('G Message')
                        ssum = ord(data[i+1])
                        valLat = 0
                        valLong = 0 
                                                                    
                        valLat = struct.unpack('f', ''.join(data[(i+2):(i+2+4)]))[0]
                        ssum = sum(map(ord,data[(i+2):(i+2+4)]))                        
                        
                        valLong = struct.unpack('f', ''.join(data[(i+6):(i+6+4)]))[0]
                        ssum = sum(map(ord,data[(i+6):(i+6+4)]))
                        
                        ssum = ssum & 0x00FF
                         
                        checksum = ord(data[i+10])
                         
                        if(ssum != checksum and ord(data[i + 11]) != EOT):
                            continue                                            
                        
                        self.info.setGPSLat(valLat)
                        self.info.setGPSLong(valLong)  
                        
                    elif (ord(data[i+1]) == ord('Y')): #Y
                        print('Y Message')
                        ssum = ord(data[i+1])
                        valX = 0
                        valY = 0
                        valZ = 0 
                        
                        valX = struct.unpack('f', ''.join(data[(i+2):(i+2+4)]))[0]
                        ssum = sum(map(ord,data[(i+2):(i+2+4)]))
                        
                        valY = struct.unpack('f', ''.join(data[(i+6):(i+6+4)]))[0]
                        ssum = sum(map(ord,data[(i+6):(i+6+4)]))
                        
                        valZ = struct.unpack('f', ''.join(data[(i+10):(i+10+4)]))[0]
                        ssum = sum(map(ord,data[(i+10):(i+10+4)]))                                                                        
                               
                        #for j in range(0, 4):
                        #    ssum = ssum + ord(data[i+10+j])                    
                        #    valZ = (valZ << 2) + ord(data[i+10+j]) & 0xFF                                                        
                        
                        ssum = ssum & 0x00FF
                         
                        checksum = ord(data[i+14])
                         
                        if(ssum != checksum and ord(data[i + 15]) != EOT):
                            continue                                            
                        
                        self.info.setGyroX(valX)
                        self.info.setGyroY(valY)
                        self.info.setGyroZ(valZ)
                                                                                  
            if(self.log == True):
                #logging.info(self.info.toJSON().encode('ascii'))
                logging.info(base64.b64encode(self.info.toJSON().encode('ascii')))
                           
        except Exception as e:
            s = str(e)
            print s
               
        
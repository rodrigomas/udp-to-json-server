#!/usr/bin/env python3
'''
Created on Feb 05, 2016

@author: Rodrigo Marques Almeida da Silva
'''

import serial
from threading import Thread

MAX_BYTES = 65535
MIN_DELAY = 0.1
MAX_DELAY = 2.0

GPS_POS_FIX = "$GPGGA"
GPS_SPEED_FIX = "$GPRMC"

class SerialReader(Thread):

    working = True

    def __init__(self, port, boundrate):
        Thread.__init__(self)
        self.port = port
        self.boundrate = boundrate
        self.info = None
        self.delay = MIN_DELAY
        self.ser = serial.Serial(port, boundrate, timeout=self.delay) 
        
    def setInfo(self, info):
        self.info = info
        
    def getInfo(self):
        return self.info    
    
    def force_stop(self):
        self.working = False
        
    def process(self, line):
        parts = line.split(',')
        
        if(self.info == None):
            return
        
        if(len(parts) > 0):
            if(parts[0].startswith('T1')):                
                try:
                    val = float(parts[1])
                    self.info.getTempBody02(val)
                    print(val) 
                except:                        
                    return            
            elif (parts[0].startswith('T0')):
                try:
                    val = float(parts[1])
                    self.info.getTempBody01(val) 
                    print(val)
                except:                        
                    return                   
            elif (parts[0].startswith('LAT')):
                try:
                    val = float(parts[1])
                    self.info.setGPSLat(val) 
                except:                        
                    return     
            elif (parts[0].startswith('LON')):
                try:
                    val = float(parts[1])
                    self.info.setGPSLong(val) 
                except:                        
                    return
            elif (parts[0].startswith('S')):
                try:
                    val = float(parts[1])
                    self.info.setGPSSpeed(val) 
                except:                        
                    return                
            elif (parts[0].startswith('B')):
                try:
                    val = float(parts[1])
                    self.info.setBPM(val) 
                except:                        
                    return
            elif (parts[0].startswith(GPS_POS_FIX)):
                try:
                    val = float(parts[2])
                    
                    if(parts[3].startswith('S')):
                        val = -val
                    
                    self.info.setGPSLat(val)
                        
                    val = float(parts[4]) 
                    if(parts[5].startswith('W')):
                        val = -val
                    
                    self.info.setGPSLong(val)
                    
                except:                        
                    return 
            elif (parts[0].startswith(GPS_SPEED_FIX)):
                try:
                    val = float(parts[7])
                    
                    val = 1.852 * val #  1 Knot =1.852 Kilometers per Hour
                    
                    self.info.setGPSSpeed(val)                 
                    
                except:                        
                    return                        
                
    def run(self):
        try:
            while self.working:               
                
                if(self.ser.is_open == False):
                    self.ser.open()
                
                #print('Waiting up to {} seconds for a reply'.format(self.delay))
                line = self.ser.readline()
                
                if(line == None or len(line) < 2 ):
                    continue
                
                try:
                    print 'New Serial Data Received'
                    print line
                    
                    self.process(line)
                                    
                except serial.Serial.SerialTimeoutException:
                    continue

                except serial.Serial.SerialException as e:
                    self.delay = MAX_DELAY                    
                    print('Serial Error: {}'.format(e))
        except KeyboardInterrupt:
                print '^C received, shutting down the data server'

        if(self.ser.is_open):
            self.ser.close()
            
        print 'Serial Server Stopping'                    
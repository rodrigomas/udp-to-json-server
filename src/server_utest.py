#!/usr/bin/env python3
'''
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
'''

import socket, random, array
from time import sleep
from threading import Thread
import struct

class UDPTestServer(Thread):
    
    working = True
    
    def run(self):
        while self.working:
            #data, address = sock.recvfrom(MAX_BYTES)
            data = self.genData()
        
            sleep(self.interval)        
            
            self.sock.sendto(data, (self.network, self.rport))
            
            print 'New Data Sended'
        
        print 'Test Server Stopping'
         
    def __init__(self, interface, network, port, rport, interval):
        Thread.__init__(self)
        self.network = network
        self.port = port
        self.rport = rport
        self.interval = interval
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #self.sock.bind((interface, port))
        self.sock.connect( (network, rport) )
        print('Test Server Working on {}'.format(self.sock.getsockname()))
    
    def force_stop(self):
        self.working = False


    @staticmethod
    def genGyro():
        dataA = [0x01, ord('Y')] 
        
        gx = random.random() * 360
        gy = random.random() * 360
        gz = random.random() * 360
        
        p = struct.pack('f',gx)
        dataA = dataA + map(ord, [c for c in p])
                
        p = struct.pack('f',gy)
        dataA = dataA + map(ord, [c for c in p])
        
        p = struct.pack('f',gz)
        dataA = dataA + map(ord, [c for c in p])        
        
        sums = (sum(dataA[1:]) & 0x00FF)
        
        dataA.append(sums)
        dataA.append(0x04)
        
        return dataA
        #[0, 0x04]    

    @staticmethod
    def genGPS():
        dataA = [0x01, ord('G')] 
        
        lat = random.random() * 1000
        lon = random.random() * 1000
        
        p = struct.pack('f',lat)
        dataA = dataA + map(ord, [c for c in p])
                
        p = struct.pack('f',lon)
        dataA = dataA + map(ord, [c for c in p])
        
        sums = (sum(dataA[1:]) & 0x00FF)
        
        dataA.append(sums)
        dataA.append(0x04)
        
        return dataA
        #[0, 0x04]              

    @staticmethod
    def genData():
        DIRS = [ord('F'), ord('D'), ord('E')]
        dataM = [0x01, ord('M'), DIRS[random.randint(0, len(DIRS) - 1)], random.randint(0, 9) + 0x30, 0, 0x04, 0]
        sums = (dataM[1] + dataM[2] + dataM[3]) & 0x00FF 
        dataM[4] = sums
            
        dataR = [0x01, ord('R'), DIRS[random.randint(0, len(DIRS) - 1)], random.randint(0, 4) + 0x30, random.randint(0, 9) + 0x30, 0, 0x04]            
        sums = (dataR[1] + dataR[2] + dataR[3]+ dataR[4]) & 0x00FF 
        dataR[5] = sums
        
        MSGA = [ord('A'), ord('V'), ord('T'), ord('D'), ord('L'), ord('B'), ord('E'), ord('F')]
        
        dataA = [0x01, MSGA[random.randint(0, len(MSGA) - 1)], random.randint(0, 9) + 0x30, random.randint(0, 9) + 0x30, random.randint(0, 9) + 0x30, 0, 0x04]            
        sums = (dataA[1] + dataA[2] + dataA[3] + dataA[4]) & 0x00FF 
        dataA[5] = sums           
            
        rval = random.randint(0, len(MSGA) + 4)
               
        if (rval == 0):
            return array.array('B', dataM) #bytearray(dataM)
        elif (rval == 1):        
            return array.array('B', dataR) #bytearray(dataR)
        elif (rval == 2):
            return array.array('B', UDPTestServer.genGPS()) #bytearray(dataR)
        elif (rval == 3):
            return array.array('B', UDPTestServer.genGyro()) #bytearray(dataR)        
        else:
            return array.array('B', dataA) #bytearray(dataA)
    
    @staticmethod
    def genFile(filename, count):
        DIRS = [ord('F'), ord('D'), ord('E')]
    
        with open(filename, 'wb') as f:
            i = 0
            while i < count:
                dataM = [0x01, ord('M'), DIRS[random.randint(0, len(DIRS) - 1)], random.randint(0, 9) + 0x30, 0, 0x04, 0]
                sums = (dataM[1] + dataM[2] + dataM[3]) & 0x00FF 
                dataM[4] = sums
                
                dataR = [0x01, ord('R'), DIRS[random.randint(0, len(DIRS) - 1)], random.randint(0, 4) + 0x30, random.randint(0, 9) + 0x30, 0, 0x04]            
                sums = (dataR[1] + dataR[2] + dataR[3]+ dataR[4]) & 0x00FF 
                dataR[5] = sums
                
                if (random.randrange(1) > 0.5):
                    f.write(array.array('B', dataM)) #bytearray(dataM)
                else:
                    f.write(array.array('B', dataR)) #bytearray(dataR)
                i =i + 1
            f.close()
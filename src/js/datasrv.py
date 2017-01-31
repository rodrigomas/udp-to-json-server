#!/usr/bin/env python3
'''
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
'''
import socket
from threading import Thread
from . import dataprocessor

MAX_BYTES = 65535
MIN_DELAY = 0.1
MAX_DELAY = 2.0

class DataSrv(Thread):

    working = True

    def __init__(self, hostname, port, processor):
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.hostname = hostname
        self.port = port
        self.delay = MIN_DELAY
        self.data = None
        self.addressList = None
        self.info = None
        #self.sock.connect( (hostname, port) )
        self.sock.bind((hostname, port))
        self.processor = processor
        print('Data server working on {}'.format(self.sock.getsockname()))
        
        self.working = True
        
    def getData(self):
        return self.data
    
    def setInfo(self, info):
        self.info = info
        
    def getInfo(self):
        return self.info    

    def force_stop(self):
        self.working = False
        
    def setAddressList(self, adl):
        self.self.addressList = adl
    
    def run(self):
        try:
            while self.working:
                print('Waiting up to {} seconds for a reply'.format(self.delay))
                
                self.sock.settimeout(self.delay)
                
                try:
                    #ldata = self.sock.recv(MAX_BYTES)
                    (ldata, address) = self.sock.recvfrom(MAX_BYTES)
                    
                    if(self.addressList != None):
                        if not (address in self.addressList):
                            self.delay = MIN_DELAY
                            continue
                    
                    self.data = ldata

                    print 'New Data Received'

                    if (self.processor != None):
                        #self.processor.process(ldata, self.info, None)
                        self.processor.process(ldata, self.info, address)
                    
                    self.delay = MIN_DELAY
                except socket.timeout:
                    self.delay *= 2
                    if self.delay > MAX_DELAY:
                        self.delay = MAX_DELAY
        except KeyboardInterrupt:
                print '^C received, shutting down the data server'
                self.sock.close()   

        print 'Data Server Stopping'        
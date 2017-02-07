#!/usr/bin/env python3
'''
Created on Feb 06, 2017

@author: Rodrigo Marques Almeida da Silva
'''

from js import serialreader, infodata


if __name__ == '__main__':
    serialserver = serialreader.SerialReader("COM3", 9600)
    
    info = infodata.InfoData()
    
    serialserver.setInfo(info)
    serialserver.start()
    
    working = True

    while working:
        command = raw_input('>')

        if(command == 'stop' or command == 'exit'):
            working = False
        
    serialserver.force_stop()    
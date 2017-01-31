#!/usr/bin/env python3
'''
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
'''
#localhost -p 14654 -ph 8000 -t
import argparse, socket
from js import httpsrv, datasrv, infodata, dataprocessor
import f1server
import logging

PORT = 8000
SPORT = 14654
SERVERNAME = "127.0.0.1"
INTERVAL = 0.5
LOGENABLE = True 

if __name__ == '__main__':
        
    parser = argparse.ArgumentParser(description="JSON Protocol Converter")
    parser.add_argument('host', help='UDP data stream hostname or IP (default: localhost)', default=SERVERNAME)
    parser.add_argument('-p', help='UDP data stream Server Port (default: 14654)', type=int, default=SPORT)
    parser.add_argument('-ph', help='HTTP JSON Server Port (default: 8000)', type=int, default=PORT)
    parser.add_argument('-l', help='Log (default: True)', type=bool, default=LOGENABLE)
    #parser.add_argument('-t', help='Run Test Server')    
    
    feature_parser = parser.add_mutually_exclusive_group(required=False)
    feature_parser.add_argument('-t', dest='testsv', action='store_true', help='Run Test Server')
    feature_parser.add_argument('-nt', dest='testsv', action='store_false')
    #parser.set_defaults(testsv=True)
    parser.set_defaults(testsv=False)
    
    args = parser.parse_args()
    
    localip = socket.gethostbyname(socket.gethostname())
    
    info = infodata.InfoData()
    
    hserver = httpsrv.HttpSrv(args.ph)
    hserver.setInfo(info)
    hserver.start()    
    
    processor = dataprocessor.F1DataProcessor()
    
    if(args.l == True):
        logging.basicConfig(name='processor', filename='data.log', level=logging.DEBUG, format='%(levelname)s:(%(asctime)s):%(message)s' )    
        processor.enableLog()
    
    serverport = args.p;

    dserver = datasrv.DataSrv(args.host, args.p, processor)    
    dserver.setInfo(info)
    dserver.start()
    
    if(args.testsv != None ):
        testsrv = f1server.UDPTestServer(args.host, args.host, args.p + 1, args.p, INTERVAL)
        testsrv.start()    
    
    print "All servers started"

    working = True

    while working:
        command = raw_input('>')

        if(command == 'stop' or command == 'exit'):
            working = False

    if(args.testsv != None ):
        testsrv.force_stop()

    dserver.force_stop()

    hserver.force_stop()
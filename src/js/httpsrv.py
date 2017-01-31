#!/usr/bin/env python3
'''
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
'''

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
from threading import Thread
import httplib

class requestHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')      
        
        info = self.server.getInfo()
        
        print 'HTTP Server Requested'
        
        response = info.toJSON().encode('ascii')         
        
        self.send_header('Content-length', len(response))
        self.end_headers()
        self.wfile.write(response)

        return

class HttpSrv(ThreadingMixIn, HTTPServer, Thread):            
        
        stopped = False
        
        def __init__(self, port):
            HTTPServer.__init__(self, ('', port), requestHandler)
            self.localport = port
            self.info = None
            #self.server = HTTPServer(('', port), requestHandler)     
            Thread.__init__(self)           
            print 'Started httpserver on port ' , port                
            
        def serve_forever(self):
            while not self.stopped:
                self.handle_request()
            
        def force_stop(self):
            self.server_close()
            self.stopped = True
            self.create_dummy_request()
            
        def create_dummy_request(self):
            try:
                print self.server_address
                conn = httplib.HTTPSConnection('http://%s:%s' % self.server_address)
                conn.request("GET", "/")
                conn.getresponse()            
            except:
                print 'Error sending dummy request'
                        
        def getInfo(self):
            return self.info
            
        def setInfo(self, info):
            self.info = info
            
        def run(self):
            try:
                self.serve_forever()
            except KeyboardInterrupt:
                print '^C received, shutting down the web server'
                self.socket.close()    

                print 'HTTP Server Stopping'
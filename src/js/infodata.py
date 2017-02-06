#!/usr/bin/env python3
'''
Created on Nov 21, 2016

@author: Rodrigo Marques Almeida da Silva
'''
import json

class InfoData(object):

    def __init__(self):
        self.MentalDir = 0x0
        self.MentalIntensity = 0
        self.ANNDir = 0x0
        self.ANNAngle = 0x0
        self.Acceleration = 0
        self.Speed = 0
        self.Temperature = 0
        self.BMP = 0
        self.Direction = 0
        self.Limit = 0
        self.TempBody01 = 0
        self.HumidityBody01 = 0
        self.TempBody02 = 0
        self.GPSLat = 0
        self.GPSLong = 0
        self.GPSSpeed = 0
        self.GyroX = 0
        self.GyroY = 0
        self.GyroZ = 0

    def getHumidityBody01(self):
        return self.HumidityBody01
    
    def setHumidityBody01(self, value):
        self.HumidityBody01 = value    

    def getGyroX(self):
        return self.GyroX
    
    def setGyroX(self, value):
        self.GyroX = value    
        
    def getGyroY(self):
        return self.GyroY
    
    def setGyroY(self, value):
        self.GyroY = value   
        
    def getGyroZ(self):
        return self.GyroZ
    
    def setGyroZ(self, value):
        self.GyroZ = value                        
        
    def getGPSLat(self):
        return self.GPSLat
    
    def setGPSLat(self, value):
        self.GPSLat = value       
        
    def getGPSLong(self):
        return self.GPSLong
    
    def setGPSSpeed(self, value):
        self.GPSSpeed = value       
        
    def getGPSSpeed(self):
        return self.GPSSpeed    
    
    def setGPSLong(self, value):
        self.GPSLong = value                

    def getTempBody01(self):
        return self.TempBody01
    
    def setTempBody01(self, value):
        self.TempBody01 = value
        
    def getTempBody02(self):
        return self.TempBody02
    
    def setTempBody02(self, value):
        self.TempBody02 = value        

    def getLimit(self):
        return self.Limit
    
    def setLimit(self, value):
        self.Limit = value

    def getDirection(self):
        return self.Direction
    
    def setDirection(self, value):
        self.Direction = value

    def getBPM(self):
        return self.BMP
    
    def setBPM(self, value):
        self.BMP = value

    def getTemperature(self):
        return self.Temperature
    
    def setTemperature(self, value):
        self.Temperature = value

    def getSpeed(self):
        return self.Speed
    
    def setSpeed(self, value):
        self.Speed = value

    def getAcceleration(self):
        return self.Acceleration
    
    def setAcceleration(self, value):
        self.Acceleration = value
    
    def getMentalDir(self):
        return self.MentalDir
    
    def setMentalDir(self, value):
        self.MentalDir = value
        
    def getMentalIntensity(self):
        return self.MentalIntensity
    
    def setMentalIntensity(self, value):
        self.MentalIntensity = value        
    
    def getANNDir(self):
        return self.ANNDir
    
    def setANNDir(self, value):
        self.ANNDir = value
        
    def getANNAngle(self):
        return self.ANNAngle
    
    def setANNAngle(self, value):
        self.ANNAngle = value
            
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
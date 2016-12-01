#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from __future__ import print_function

from BrickPi import *

BrickPiSetup()

class Shooter(object):
    WHEELCIRCUMFERENCE = 6.265
    WHEELDISTANCE = 12
    
    MOTORPITCH = 0  # PORT_A
    MOTORLEFT  = 1  # PORT_B
    MOTORRIGHT = 2  # PORT_C
    MOTORSHOOT = 3  # PORT_D
    
    
    def __init__(self,debug = False):
        BrickPiSetup()
        # BrickPi.MotorEnable[MOTORPITCH] = 1 #Enable the Motor A
        # BrickPi.MotorEnable[MOTORLEFT] = 1 #Enable the Motor B
        # BrickPi.MotorEnable[MOTORRIGHT] = 1 #Enable the Motor C
        # BrickPi.MotorEnable[MOTORSHOOT] = 1 #Enable the Motor D

    def moveForward(distance):
        deg = distance * 114.61 /WHEELCIRCUMFERENCE
        motorRotateDegree([255,255],[deg,deg],[MOTORLEFT,MOTORRIGHT])
        if debug: print("moveForward: "+distance)
  
    def moveBackward(distance):
        deg = distance * 114.61 /WHEELCIRCUMFERENCE
        motorRotateDegree([255,255],[-deg,deg],[MOTORLEFT,MOTORRIGHT])
        if debug: print("moveBackward: "+distance)
    
    def turnLeft(angle):
        deg = angle * WHEELDISTANCE / WHEELCIRCUMFERENCE
        motorRotateDegree([255,255],[deg,-deg],[MOTORLEFT,MOTORRIGHT])
        if debug: print("turnLeft: "+angle)

    def turnRight(angle):
        deg = angle * WHEELDISTANCE / WHEELCIRCUMFERENCE
        motorRotateDegree([255,255],[-deg,deg],[MOTORLEFT,MOTORRIGHT])
        if debug: print("turnRight: "+angle)

	def pitchRel(degree):
        motorRotateDegree([255,255],[degree,degree],[MOTORPITCH,MOTORSHOOT])
        if debug: print("pitchRel: "+degree)
        
    # def pitchAbs(angle):
    
    
    def shoot():
        BrickPi.MotorEnable[MOTORSHOOT] = 1
        
        #close
        BrickPi.MotorSpeed[MOTORSHOOT] = 255
        BrickPiUpdateValues()
        if debug: print("Closing: Start")
        
        #wait until fully closed
        deg = BrickPi.Encoder[MOTORSHOOT]
        closed = False
        while not closed:
            BrickPiUpdateValues():
            diff = abs(deg - BrickPi.Encoder[MOTORSHOOT])
            if diff < 5:
                closed = True
            if debug: print("Closing: difference: "+diff)
            time.sleep(0.1)
        
        #open
        BrickPi.MotorSpeed[MOTORSHOOT] = -255
        BrickPiUpdateValues()
        if debug: print("Opening: Start")
        
        #wait until fully opend
        deg = BrickPi.Encoder[MOTORSHOOT]
        opend = False
        while not opend:
            BrickPiUpdateValues():
            diff = abs(deg - BrickPi.Encoder[MOTORSHOOT])
            if diff < 5:
                opend = True
            if debug: print("Opening: difference: "+diff)
            time.sleep(0.1)
        
        #End Shooting
        BrickPi.MotorEnable[MOTORSHOOT] = 0
        BrickPiUpdateValues()
        if debug: print("Finish shooting")
        
    
if __name__ == '__main__':
    print("==================")
    print("Start Test Shooter")    
    print("==================")
    
    distance = 10
    deg = 90
    pitch = 10
    
    print("create shooter")
    shooter = Shooter(True)

    print("moveForward "+distance+"cm")
    shooter.moveForward(distance)
    time.sleep(1)

    print("moveBackward "+distance+"cm")
    shooter.moveBackward(distance)
    time.sleep(1)

    print("turnLeft "+deg+"deg")
    shooter.turnLeft(deg)
    time.sleep(1)
    
    print("turnRight "+deg+"deg")
    shooter.turnRight(deg)
    time.sleep(1)
    
    print("pitchRel "+pitch+" up and down")
    shooter.pitchRel(pitch)
    time.sleep(1)
    shooter.pitchRel(-pitch)
    time.sleep(1)
    
    print("shoot")
    shooter.shoot()
    print("Finish Test Shooter")
"""
TESSR
(The Extremely Small Security Robot)

Version 1.0
>Added remote control via Bluedot from a phone
>Added ability to remotely take photos
Version 2.0
>Added object detection via bumper (after issues with UDS)
"""
#Get dependencies
import time
import ZeroBorg3 as ZeroBorg
from cameraUtils import captureImage
from signal import pause
from bluedot import BlueDot
from gpiozero import Button

class TESSR:
    """Controls all basic behaviors of TESSR"""

    mode = "auto"

    ZB = ZeroBorg.ZeroBorg()
    bumper = Button(14)

    def __init__(self):
        #Ready ZeroBorg
        self.ZB.Init()
        self.ZB.ResetEpo()
        self.ZB.MotorsOff()
        #Stores motor speeds
        self.speed = 0
        #
        if self.mode == "remote":
            #Pair with phone via Bluetooth server
            self.bd = BlueDot()
            while True:
                self.bd.when_pressed = self.remoteControl
        elif self.mode == "auto":
            self.automaticControl()
    
    def forward(self):
        if (self.speed < 0):
            self.speed = 0
        elif (self.speed < 100):
            self.speed += 5
        self.ZB.SetMotors(self.speed)

    def reverse(self):
        if (self.speed > 0):
            self.speed = 0
        elif (self.speed > -100):
            self.speed -= 5
        self.ZB.SetMotors(self.speed)

    def turnLeft(self):
        #Check weighting
        self.ZB.SetMotor1(0)
        time.sleep(1)
        #self.ZB.SetMotors(self.speed)

    def turnRight(self):
        #Check weighting
        self.ZB.SetMotor2(0)
        time.sleep(1)
        #self.ZB.SetMotors(self.speed)

    def stop(self):
        self.speed = 0
        self.ZB.SetMotors(self.speed)

    def remoteControl(self,pos):
        if pos.top:
            self.forward()
        elif pos.bottom:
            self.reverse()
        elif pos.left:
            self.turnLeft()
        elif pos.right:
            self.turnRight()
        elif pos.middle:
            captureImage()

    def automaticControl(self):
        while True:
            self.forward()
            if self.bumper.is_held:
                self.turnLeft()
                time.sleep(1)

robot = TESSR()
pause() 

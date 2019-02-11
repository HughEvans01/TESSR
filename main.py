"""
TESSR
(The Extremely Small Security Robot)

Version 1.0
>Added remote control via Bluedot from a phone
>Added ability to remotely take photos
"""
#Get dependencies
import time
import captureImage from cameraUtils
import ZeroBorg3 as ZeroBorg
from signal import pause
from bluedot import BlueDot

class TESSR:
    """Controls all basic behaviors of TESSR"""

    mode = "remote"

    ZB = ZeroBorg.ZeroBorg()
    camera = PiCamera

    def init(self,):
        #Ready ZeroBorg
        ZB.Init()
        ZB.ResetEpo()
        ZB.MotorsOff()
        #Stores motor speeds
        self.speed = 0
        #
        if mode == "remote":
            #Pair with phone via Bluetooth server
            bd = BlueDot()
            while True:
                bd.when_pressed = self.remoteControl
        elif mode == "auto":
            self.automaticControl()
    
    def forward(self):
        if (self.speed < 0):
            self.speed = 0
        elif (self.speed < 100):
            self.speed += 5
        ZB.SetMotors(self.speed)

    def reverse(self):
        if (self.speed > 0):
            self.speed = 0
        elif (self.speed > -100):
            self.speed -= 5
         ZB.SetMotors(self.speed)

    def turnLeft(self):
        #Check weighting
        ZB.SetMotor2(0)
        time.sleep(1)
        ZB.SetMotor(self.speed)

    def turnRight(self):
        #Check weighting
        ZB.SetMotor1(0)
        time.sleep(1)
         ZB.SetMotor(self.speed)

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
        pass
tessr = TESSR()

pause()
 

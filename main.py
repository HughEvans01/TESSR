"""
TESSR
(The Extremely Small Security Robot)

Version 1.0
>
"""
#Get dependencies
import time
import ZeroBorg3 as ZeroBorg
from signal import pause
from bluedot import BlueDot
from picamera import PiCamera

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
        self.motor1 = 0
        self.motor2 = 0
        #
        if mode == "remote":
            #Pair with phone via Bluetooth server
            bd = BlueDot()
            while True:
                bd.when_pressed = self.remoteControl
        elif mode == "auto":
            self.automaticControl()

    def remoteControl(self):


    def automaticControl(self):
        pass
Test = TESSR()

pause()
 

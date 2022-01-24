#import evdev
from evdev import InputDevice, categorize, ecodes
from Johnny_Led import *
from Johnny_Camera import *
from Johnny_Motor import *

class JohnnyMotorController:
    #button code variables (change to suit your device)
    aBtn = 304
    bBtn = 305
    yBtn = 307
    xBtn = 306 
    turboBtn = 317
    rtBtn = 311
    tlBtn = 310

    def __init__(self):
        #creates object 'gamepad' to store the data
        #you can call it whatever you like
        self.gamepad = InputDevice('/dev/input/event0')
        #prints out device info at start
        print(self.gamepad.capabilities(verbose=True))
        led = Led() 
        self.ledController = JohnnyLed()
        self.connectedMotor = None
        self.turbo=False
        self.multiplier = 1


    def run(self):
        #evdev takes care of polling the controller in a loop
        for event in self.gamepad.read_loop():

            if event.type == ecodes.EV_KEY:
                if event.code == self.aBtn: #light show
                    if event.value == 1:
                        self.ledController.chase_color_around(Color(255, 0, 0), Color(0, 0, 255),10)
                elif event.code == self.xBtn: #take a picture
                    #only do it when pressed
                    if event.value == 1:
                        camera = JohnnyCamera()
                        ts = str(time.time())
                        camera.takeAPicture(ts + "_picture")
                        camera.destroy()
                elif event.code == self.yBtn:
                    if event.value == 1: #only when pressed
                        #construct the engine if not constructed
                        if self.connectedMotor == None:
                            self.connectedMotor=JohnyMotor()   
                            self.ledController.colorWipe(self.ledController.strip, Color(255,0,0),75)
                            self.ledController.colorWipe(self.ledController.strip, Color(255,255,0),75)
                            self.ledController.colorWipe(self.ledController.strip, Color(0,255,0),75)
                elif event.code == self.turboBtn:
                    if event.value == 1: #pressed
                        if self.turbo==False:
                            self.turbo = True
                            self.multiplier=4
                        else:
                            self.turbo = False
                            self.multiplier=1
                elif event.code == self.rtBtn:
                    if self.connectedMotor!=None:
                        if event.value ==1:
                            self.connectedMotor.set_all_motors(4500,4500,-4500,-4500)
                        elif event.value == 0:
                            self.connectedMotor.set_all_motors(0,0,0,0)
                elif event.code == self.tlBtn:
                    if self.connectedMotor!=None:
                        if event.value ==1:
                            self.connectedMotor.set_all_motors(-4500,-4500,4500,4500)
                        elif event.value == 0:
                            self.connectedMotor.set_all_motors(0,0,0,0)
                keyEvent = categorize(event)
                print(keyEvent)
                # print("####")
            elif event.type == ecodes.EV_ABS:
                if ecodes.ABS[event.code] == 'ABS_Y':
                    print("Y VALUE: "+str(event.value))
                elif ecodes.ABS[event.code] == 'ABS_X':
                    print("X VALUE: "+str(event.value))
                elif event.code == 16:
                    if self.connectedMotor==None:    
                        print("No Connected Motor")
                    else:
                        if event.value == -1: # Left
                            self.connectedMotor.set_all_motors(-1000*self.multiplier,-1000*self.multiplier,1000*self.multiplier,1000*self.multiplier)
                        elif event.value == 1: # Right
                            self.connectedMotor.set_all_motors(1000*self.multiplier,1000*self.multiplier,-1000*self.multiplier,-1000*self.multiplier)
                        else:
                            self.connectedMotor.set_all_motors(0,0,0,0)
                elif event.code == 17: # DPAD
                    if self.connectedMotor==None:
                        print("No Connected Motor")
                    else:
                        print("[inputs]", event.code, event.value)
                        if event.value == -1: # UP
                            self.connectedMotor.set_all_motors(1000*self.multiplier,1000*self.multiplier,1000*self.multiplier,1000*self.multiplier)
                        elif event.value == 1: # DOWN
                            self.connectedMotor.set_all_motors(-1000*self.multiplier,-1000*self.multiplier,-1000*self.multiplier,-1000*self.multiplier)
                        else:
                            self.connectedMotor.set_all_motors(0,0,0,0)
                else:
                    print(event.code)
                    if event.value == 0:
                        print("LEFT")
                    elif event.value == 255:
                        print("RIGHT")
                    else:
                        print(event.value)
                        print("release")

# This is where I run my code as it is outside the class
NUMBER_FIVE = JohnnyMotorController()
NUMBER_FIVE.run()
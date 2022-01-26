#import evdev
from evdev import InputDevice, categorize, ecodes
from Johnny_Led import *
from Johnny_Camera import *
from Johnny_Motor import *
from servo import *

class JohnnyMotorController:
    #button code variables (change to suit your device)
    aBtn = 304
    bBtn = 305
    yBtn = 307
    xBtn = 306 
    turboBtn = 317
    rtBtn = 311
    tlBtn = 310
    startBtn = 313
    maxJoystick = 65535
    minJoystick = 0

    currentHorizontalServo = 90
    currentVerticalServo = 90


    def __init__(self):
        #creates object 'gamepad' to store the data
        #you can call it whatever you like
        self.gamepad = InputDevice('/dev/input/event0')
        #prints out device info at start
        capabilities = self.gamepad.capabilities(verbose=True)
        print(capabilities)

        led = Led() 
        self.ledController = JohnnyLed()
        self.connectedMotor = None
        self.turbo=False
        self.multiplier = 1

        self.pwm=Servo()

    def listenForEvents(self):
        #evdev takes care of polling the controller in a loop
        for event in self.gamepad.read_loop():
            #determine the event type
            if event.type == ecodes.EV_KEY:
                #determine the specific key that was pressed
                if event.code == self.aBtn: 
                    self.__chaseColorButtonPress__(event)
                elif event.code == self.xBtn: #take a picture
                    self.__takeAPicture__(event)
                elif event.code == self.yBtn:
                    print("Empty Y button")
                elif event.code == self.bBtn:
                    self.__randomLED__(event)
                elif event.code == self.turboBtn:
                    self.__turboEnableDisable__(event)
                elif event.code == self.rtBtn:
                    self.__rightDonuts__(event)
                elif event.code == self.tlBtn:
                    self.__leftDonuts__(event)
                elif event.code == self.startBtn:
                    self.__startMotor__(event)
                else:
                    self.__printEvent__(event)

            elif event.type == ecodes.EV_ABS:
                if ecodes.ABS[event.code] == 'ABS_Y': #Left Joystick
                    print("Y VALUE: "+str(event.value))
                elif ecodes.ABS[event.code] == 'ABS_X': #Left Joystick
                    print("X VALUE: "+str(event.value))
                    print("[inputs]", event.code, event.value)
                elif ecodes.ABS[event.code] == 'ABS_RY': #Right Joystick
                    self.__joystickRightYAxis__(event.value)
                elif ecodes.ABS[event.code] == 'ABS_RX': #Right Joystick X Axis
                    self.__joystickRightXAxis__(event.value)
                elif event.code == 16:
                    self.__directionalPadLeftRight__(event)
                elif event.code == 17: # DPAD
                    self.__directionalPadUpDown__(event)
                else:
                    self.__printEvent__(event)

    #Private Methods
    def __chaseColorButtonPress__(self, event):
        if event.value == 1:
            self.ledController.chase_color_around(Color(255, 0, 0), Color(0, 0, 255),10)
    
    def __takeAPicture__(self, event):
        #only do it when pressed
        if event.value == 1:
            # camera = JohnnyCamera()
            # ts = str(time.time())
            # camera.takeAPicture(ts + "_picture")
            # camera.destroy()
            print("CAMERA IS DEAD")

    def __randomLED__(self, event):
        if event.value == 1: #button pressed
            self.ledController.random_led_display(5)

    def __turboEnableDisable__(self, event):
        if event.value == 1: #pressed
            if self.turbo==False:
                self.turbo = True
                self.multiplier=4
            else:
                self.turbo = False
                self.multiplier=1

    def __rightDonuts__(self, event):
        if self.connectedMotor!=None: #only when the Motor is enabled
            if event.value ==1: # button pressed
                self.ledController.colorWipe(self.ledController.strip, Color(255,255,0),0) #Yellow
                self.connectedMotor.set_all_motors(4500,4500,-4500,-4500)
            elif event.value == 0: # button depressed
                self.ledController.colorWipe(self.ledController.strip, Color(255,0,0),0) #RED
                self.connectedMotor.set_all_motors(0,0,0,0)

    def __leftDonuts__(self, event):
        if self.connectedMotor!=None:
            if event.value ==1:
                self.ledController.colorWipe(self.ledController.strip, Color(255,255,0),0) #Yellow
                self.connectedMotor.set_all_motors(-4500,-4500,4500,4500)
            elif event.value == 0:
                self.ledController.colorWipe(self.ledController.strip, Color(255,0,0),0) #RED
                self.connectedMotor.set_all_motors(0,0,0,0)

    def __startMotor__(self, event):
        if event.value == 1: #only when pressed
            #construct the engine if not constructed
            if self.connectedMotor == None:
                self.connectedMotor=JohnyMotor()   
                self.ledController.colorWipe(self.ledController.strip, Color(255,0,0),75) #RED
                self.ledController.colorWipe(self.ledController.strip, Color(255,255,0),75) #Yellow
                self.ledController.colorWipe(self.ledController.strip, Color(0,255,0),75) #GREEN

    def __printEvent__(self,event):
        keyEvent = categorize(event)
        print("Unhandled Key Press: " +str(keyEvent))
        print("[inputs]", event.code, event.value)

    def __directionalPadLeftRight__(self, event):
        if self.connectedMotor==None:    
            print("No Connected Motor")
        else:
            if event.value == -1: # Left
                self.ledController.colorWipe(self.ledController.strip, Color(255,255,0),0) #Yellow
                self.connectedMotor.set_all_motors(-1000*self.multiplier,-1000*self.multiplier,1000*self.multiplier,1000*self.multiplier)
            elif event.value == 1: # Right
                self.ledController.colorWipe(self.ledController.strip, Color(255,255,0),0) #Yellow
                self.connectedMotor.set_all_motors(1000*self.multiplier,1000*self.multiplier,-1000*self.multiplier,-1000*self.multiplier)
            else:
                self.ledController.colorWipe(self.ledController.strip, Color(255,0,0),0) #RED
                self.connectedMotor.set_all_motors(0,0,0,0)
    
    def __directionalPadUpDown__(self,event):
        if self.connectedMotor==None:
            print("No Connected Motor")
        else:
            if event.value == -1: # UP
                self.ledController.colorWipe(self.ledController.strip, Color(0,255,0),0) #GREEN
                self.connectedMotor.set_all_motors(1000*self.multiplier,1000*self.multiplier,1000*self.multiplier,1000*self.multiplier)
            elif event.value == 1: # DOWN
                self.ledController.colorWipe(self.ledController.strip, Color(0,255,0),0) #GREEN
                self.connectedMotor.set_all_motors(-1000*self.multiplier,-1000*self.multiplier,-1000*self.multiplier,-1000*self.multiplier)
            else:
                self.ledController.colorWipe(self.ledController.strip, Color(255,0,0),0) #RED
                self.connectedMotor.set_all_motors(0,0,0,0)

    def __joystickRightXAxis__(self,value):
        normalizedValue = self.__normalizeAxisValue__(value)
        #If it is < 0 && > -1 then back
        if (normalizedValue<0) and (normalizedValue>-1):
            tempval = self.currentHorizontalServo -3
            if tempval > 0 and tempval< 180:
                self.currentHorizontalServo = tempval
                self.pwm.setServoPwm('0',self.currentHorizontalServo)
        elif (normalizedValue<1) and (normalizedValue>0):
            tempval = self.currentHorizontalServo +3
            if tempval > 0 and tempval< 180:
                self.currentHorizontalServo = tempval
                self.pwm.setServoPwm('0',self.currentHorizontalServo)
        else:
            print("Ignore")

    def __joystickRightYAxis__(self,value):
        normalizedValue = self.__normalizeAxisValue__(value)
        #If it is < 0 && > -1 then back
        if (normalizedValue<0) and (normalizedValue>-1):
            tempval = self.currentVerticalServo +3
            if tempval > 0 and tempval< 180:
                self.currentVerticalServo = tempval
                self.pwm.setServoPwm('1',self.currentVerticalServo)
        elif (normalizedValue<1) and (normalizedValue>0):
            tempval = self.currentVerticalServo -3
            if tempval > 0 and tempval< 180:
                self.currentVerticalServo = tempval
                self.pwm.setServoPwm('1',self.currentVerticalServo)
        else:
            print("Ignore")

    def __normalizeAxisValue__(self,value):
        normalizedValue = 2.0 * (value - self.minJoystick) / (self.maxJoystick - self.minJoystick) - 1.0
        return normalizedValue
# This is where I run my code as it is outside the class
NUMBER_FIVE = JohnnyMotorController()
NUMBER_FIVE.listenForEvents()
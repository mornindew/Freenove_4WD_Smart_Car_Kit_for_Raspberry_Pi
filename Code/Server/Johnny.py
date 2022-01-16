"""
This is johnny and is the main class that controls the rover
"""
import time
import sys

from rpi_ws281x.rpi_ws281x import Color
from picamera import PiCamera
from Johnny_Led import JohnnyLed
from Motor import Motor
from Buzzer import Buzzer
from Led import Led
from Line_Tracking import Line_Tracking
from Light import Light
from Ultrasonic import Ultrasonic
from ADC import Adc
from Constant import *


class Johnny:
    """This is the class definition and where I define the class.
        Johnny 5 is the main class for running the rovers
    """

    # pylint: disable=too-many-instance-attributes
    # The linter is wrong,  muhahaha!
    # built in init function - This will be called every time that the class is used
    def __init__(self, name):
        # set the member vars
        # a member variables is a variable that is stored in the class and can be used
        # by all methods in the class
        self.name = name
        print(self.name + " is alive!\n")
        self.motor = Motor()
        ## I set this one as private to show how it can be done but python is stupid
        ## on how it handles private vars
        self.__buzzer = Buzzer()
        self.led = JohnnyLed()
        self.camera = PiCamera()
        self.infrared = Line_Tracking()
        self.light_car = Light()
        self.ultrasonic = Ultrasonic()
        self.__get_battery_power()

    def run(self):
        """This is the main method to run the program.
        It will prompt the user
        """
        # Prompt the user to tell Johnny what to do
        print("Choose the form of your destructor")
        print("1: Count")
        print("2: Run the Motor Manually")
        print("3: Talk to me")
        print("4: Fireworks")
        print("5: Take a Picture")
        print("6: Stay in Line")
        print("7: Follow the light ")
        print("8: Find my own way")
        print("9: Show Off")
        print("10: Tell me what to do")
        print("11: Shine On")
        print("")
        # create an input variable so that the user can interact with the program
        var = input("Enter Your Input:  ")
        if var == "1":
            self.__count()
        elif var == "2":
            self.manual_motor_run()
        elif var == "3":
            self.talk_to_me()
        elif var == "4":
            self.fireworks()
        elif var == "5":
            file_name = input("What do you want to call the picture:  ")
            self.take_a_picture(file_name)
        elif var == "6":
            self.follow_a_line()
        elif var == "7":
            self.follow_the_light()
        elif var == "8":
            self.auto_detect_route()
        elif var == "9":
            self.show_off()
        elif var == "10":
            self.tell_me_what_to_do()
        elif var == "11":
            self.shine_bright()
        else:
            print("not a valid option")

    def shine_bright(self):
        try:
            self.led.display_led(FRONT_OF_BACK_RIGHT_WHEEL,255,0,0)      #Red
            self.led.display_led(REAR_OF_BACK_RIGHT_WHEEL,255,125,0)    #orange
            self.led.display_led(REAR_OF_BACK_LEFT_WHEEL,255,255,0)    #yellow
            self.led.display_led(FRONT_OF_BACK_LEFT_WHEEL,0,255,0)      #green
            self.led.display_led(REAR_OF_FRONT_LEFT_WHEEL,0,255,255)    #cyan-blue
            self.led.display_led(FRONT_OF_FRONT_LEFT_WHEEL,0,0,255)      #blue
            self.led.display_led(FRONT_OF_FRONT_RIGHT_WHEEL,128,0,128)    #purple
            self.led.display_led(REAR_OF_FRONT_RIGHT_WHEEL,255,255,255)  #white'''
            print ("The LED has been lit, the color is red orange yellow green cyan-blue blue white")
            time.sleep(3)               #wait 3s
            self.led.colorWipe(self.led.strip, Color(0,0,0))  #turn off the light
            print ("\nEnd of program")
        except KeyboardInterrupt:
            self.led.colorWipe(self.led.strip, Color(0,0,0))  #turn off the light
            print ("\nEnd of program")
    def fireworks(self):
        """This method will do a lightshow
        """
        try:
            print("Chaser animation")
            #Blue Chasing Red 100 times
            self.led.chase_color_around(Color(255, 0, 0), Color(0, 0, 255),100)
            self.led.random_led_display(100)
            self.led.colorWipe(self.led.strip, Color(255, 0, 0))  # Red wipe
            self.led.colorWipe(self.led.strip, Color(0, 255, 0))  # Green wipe
            self.led.colorWipe(self.led.strip, Color(0, 0, 255))  # Blue wipe
            self.led.theaterChaseRainbow(self.led.strip,25)
            self.led.rainbowCycle(self.led.strip,3)
            self.led.colorWipe(self.led.strip, Color(0, 0, 0), 10)
        except KeyboardInterrupt:
            self.led.colorWipe(self.led.strip, Color(0, 0, 0), 10)

    def take_a_picture(self, name: str):
        """
        Internal Method to take a picture

        Args:
            name (str): this is the name of the file that you want the image to be called
        """
        self.camera.capture(name + ".jpg")

    def follow_a_line(self):
        """
        this method will track to a line
        """
        print(self.name + " is in the shop")

    def follow_the_light(self):
        """
        This method will use the infared and follow a light
        """
        self.infrared.run()

    def auto_detect_route(self):
        """
        this will use the ultrasonic object detection and find its own way
        """
        try:
            self.ultrasonic.run()
        except KeyboardInterrupt:
            # self.motor.setMotorModel(0, 0, 0, 0)
            ##self.ultrasonic.PWM.motor_S.setServomotor("0", 90)
            self.ultrasonic.PWM.setMotorModel(0, 0, 0, 0)
            self.ultrasonic.pwm_S.setServoPwm("0", 90)

    def show_off(self):
        """This method will do a quick show off of it's capabilities
        """
        try:
            self.motor.setMotorModel(-1500, -1500, 2000, 2000)  # Left
            print("The car is turning left")
            self.__custom_sleep(800)
            self.motor.setMotorModel(2000, 2000, -1500, -1500)  # Right
            print("The car is turning Right")
            self.__custom_sleep(800)
            self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
            print("The car is moving forward")
            self.__custom_sleep(250)
            self.motor.setMotorModel(-1000, -1000, -1000, -1000)  # Backward
            print("The car is moving Backward")
            self.__custom_sleep(250)
            self.motor.setMotorModel(-1500, -1500, 2000, 2000)  # Left
            print("The car is turning left")
            self.__custom_sleep(800)
            self.motor.setMotorModel(2000, 2000, -1500, -1500)  # Right
            print("The car is turning Right")
            self.__custom_sleep(800)
            self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
            print("The car is moving forward")
            self.__custom_sleep(250)
            self.motor.setMotorModel(-1000, -1000, -1000, -1000)  # Backward
            print("The car is moving Backward")
            self.__custom_sleep(250)
            self.motor.setMotorModel(0, 0, 0, 0)  # Stop
            self.fireworks()
            self.talk_to_me()
            self.take_a_picture("showoff")
            print("\nEnd of program")
        except KeyboardInterrupt:
            sys.exit()

    def tell_me_what_to_do(self):
        """
        This method will prompt the user for specific instructions
        and follow those instructions
        """
        try:
            while True:
                print("Choose your path")
                print("1: Forward")
                print("2: Backward")
                print("3: Left Turn")
                print("4: Right Turn")
                print("5: Exit")
                input_value = input("Enter Your Input:  ")
                if input_value == "5":
                    break
                number_of_seconds = float(input("Enter Number of Seconds: "))
                if input_value == "1":
                    self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
                    time.sleep(number_of_seconds)
                elif input_value == "2":
                    self.motor.setMotorModel(-1000, -1000, -1000, -1000)  # Backward
                    time.sleep(number_of_seconds)
                elif input_value == "3":
                    self.motor.setMotorModel(-1500, -1500, 2000, 2000)  # Left
                    time.sleep(number_of_seconds)
                elif input_value == "4":
                    self.motor.setMotorModel(2000, 2000, -1500, -1500)  # Right
                    time.sleep(number_of_seconds)
                # On every loop
                self.motor.setMotorModel(0, 0, 0, 0)  # Stop
        except KeyboardInterrupt:
            sys.exit()

    def manual_motor_run(self):
        """Method to run the motor manually.   Right now it goes in a square
        Params:
            Self - passes itself in to have access to the motor
        """
        # Try / Except pattern - used so that the keyboard interupt can be captured
        try:
            self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
            print("The car is moving forward")
            # I use an internal method called custom sleep to loop in millis
            # The thought was that I could reduce the amount of time we are sleeping
            # and missing keyboard interrupts
            # it doesn't work as well as i intended
            self.__custom_sleep(3500)
            # call the motor
            self.motor.setMotorModel(-1500, -1500, 2000, 2000)  # Left
            print("The car is turning left")
            self.__custom_sleep(800)
            self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
            print("The car is moving forward")
            self.__custom_sleep(8000)
            self.motor.setMotorModel(-1500, -1500, 2000, 2000)  # Left
            print("The car is turning left")
            self.__custom_sleep(800)
            self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
            print("The car is moving forward")
            self.__custom_sleep(4000)
            self.motor.setMotorModel(-1500, -1500, 2000, 2000)  # Left
            print("The car is turning left")
            self.__custom_sleep(800)
            self.motor.setMotorModel(1000, 1000, 1000, 1000)  # Forward
            print("The car is moving forward")
            self.__custom_sleep(8000)
            self.motor.setMotorModel(0, 0, 0, 0)  # Stop
            print("\nEnd of program")
        except KeyboardInterrupt:
            sys.exit()

    def talk_to_me(self):
        """Method to run the buzzer
        """
        try:
            self.__buzzer.run("1")
            time.sleep(1)
            print("1S")
            time.sleep(1)
            print("2S")
            time.sleep(1)
            print("3S")
            self.__buzzer.run("0")
            print("\nEnd of program")
        except KeyboardInterrupt:
            self.__buzzer.run("0")
            print("\nEnd of program")

    def __custom_sleep(self, millis):
        # convert millis to count each milli
        for i in range(millis):
            try:
                time.sleep(0.001)
            except KeyboardInterrupt:
                print("Oh! You have sent a Keyboard Interrupt to me.\nBye, Bye")
                sys.exit()
            if i > millis:
                break
    
    def __get_battery_power(self):
        adc=Adc()
        Left_IDR=adc.recvADC(0)
        print ("The photoresistor voltage on the left is "+str(Left_IDR)+"V")
        Right_IDR=adc.recvADC(1)
        print ("The photoresistor voltage on the right is "+str(Right_IDR)+"V")
        Power=adc.recvADC(2)
        print ("The battery voltage is "+str(Power*3)+"V")
        

    #Static methods
    # count method that will only count for 10 seconds -
    # this is really on used to show the power of computing
    @staticmethod
    def __count():
        start_time = time.time()
        # Set how long to count
        max_seconds = 10
        # start the counter
        count = 0
        while True:
            # get the current count
            current_time = time.time()
            elapsed_time = current_time - start_time
            count = count + 1
            if elapsed_time > max_seconds:
                print("Total Count: " + str(count))
                break
        
# This is where I run my code as it is outside the class
NUMBER_FIVE = Johnny("Johnny 5")
NUMBER_FIVE.run()
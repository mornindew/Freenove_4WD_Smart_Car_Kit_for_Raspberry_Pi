import time
from Led import *
led=Led()
def test_Led():
    try:
        # led.ledIndex(0x01,255,0,0)      #Red
        # led.ledIndex(0x02,255,125,0)    #orange
        # led.ledIndex(0x04,255,255,0)    #yellow
        # led.ledIndex(0x08,0,255,0)      #green
        # led.ledIndex(0x10,0,255,255)    #cyan-blue
        # led.ledIndex(0x20,0,0,255)      #blue
        # led.ledIndex(0x40,128,0,128)    #purple
        #led.ledIndex(0x80,255,255,255)  #white'''

        #Setting them individually

        # led.strip.setPixelColor(0, Color(255,0,0)) #Red
        # led.strip.show()
        # led.strip.setPixelColor(1, Color(255,125,0)) #Orange
        # led.strip.show()
        # led.strip.setPixelColor(2, Color(255,255,0)) #Yellow
        # led.strip.show()
        # led.strip.setPixelColor(3, Color(0,255,0)) #Green
        # led.strip.show()
        # led.strip.setPixelColor(4, Color(0,255,255)) #cyan-blue
        # led.strip.show()
        # led.strip.setPixelColor(5, Color(0,0,255)) #blue
        # led.strip.show()
        # led.strip.setPixelColor(6, Color(128,0,128)) #purple
        # led.strip.show()
        # led.strip.setPixelColor(7, Color(255,255,255)) #white
        # led.strip.show()

        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
        #Setting in a loop
        for x in range (8):
            led.strip.setPixelColor(x, Color(255,0,0)) #Red
            led.strip.show()
            time.sleep(1)


        print ("The LED has been lit, the color is red orange yellow green cyan-blue blue white")
        time.sleep(3)               #wait 3s
        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
        print ("\nEnd of program")
    except KeyboardInterrupt:
        led.colorWipe(led.strip, Color(0,0,0))  #turn off the light
        print ("\nEnd of program")

from Motor import *            
roverMotors=Motor() 
roverLed=Led()         
def test_Motor(): 
    try:
        roverLed.colorWipe(led.strip, Color(255, 0, 0),0)  # set to red because we are stopped
        time.sleep(1)
        roverLed.colorWipe(led.strip, Color(255,255,0),0)  # Set to yellow to make a red --> yellow --> Green
        time.sleep(.5)
        roverLed.colorWipe(led.strip, Color(0, 255, 0),0)  # Set to green
        roverMotors.setMotorModel(600,600,600,600)       #Forward
        time.sleep(3.4) #I won't comment the other sleeps but this causes the motor to continue running for 1.5 seconds
        roverLed.colorWipe(led.strip, Color(255,255,0),0)  # sets the LED to yellow becasue we are turning
        roverMotors.setMotorModel(1000,1000,-500,-500)   #Right turn 
        time.sleep(1.60)
        roverLed.colorWipe(led.strip, Color(0, 255, 0),0)  #set the color to Green as we are moving forward again
        roverMotors.setMotorModel(600,600,600,600)       #Forward 
        time.sleep(1.55)
        roverLed.colorWipe(led.strip, Color(255,255,0),0)  # Set to yellow as we are turning
        roverMotors.setMotorModel(-500,-500,1000,1000)   #Make left turn
        time.sleep(1.60)
        roverLed.colorWipe(led.strip, Color(0, 255, 0),0)  # Set to green
        roverMotors.setMotorModel(600,600,600,600)       #Forward 
        time.sleep(1.40)
        roverLed.colorWipe(led.strip, Color(255,255,0),0)  # Yellow wipe
        roverMotors.setMotorModel(-500,-500,1000,1000)   #Left 
        time.sleep(1.60)
        roverLed.colorWipe(led.strip, Color(0, 255, 0),0)  # Green wipe
        roverMotors.setMotorModel(600,600,600,600)       #Forward 
        time.sleep(1.75)
        roverLed.colorWipe(led.strip, Color(255,255,0),0)  # Yellow wipe
        roverMotors.setMotorModel(1000,1000,-500,-500)   #Right 
        time.sleep(1.60)
        roverLed.colorWipe(led.strip, Color(0, 255, 0))  # Set LED to Green
        roverMotors.setMotorModel(600,600,600,600)     #Forward 
        time.sleep(1)
        roverLed.colorWipe(led.strip, Color(255,255,0),0)  # Yellow wipe
        roverMotors.setMotorModel(-4500,-4500,4500,4500)  #DONUTS!!!
        time.sleep(2)
        roverLed.colorWipe(led.strip, Color(255, 0, 0))  # set to red because we are stopping
        roverMotors.setMotorModel(0,0,0,0)
        print ("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")

def test_ChaseLeds(primaryColor, chaseColor, number_of_laps_around_the_rover):
    roverLed=Led()   
    empty_color = Color(0, 0, 0) #Empty Color
    #each loop is a lap around the rover
    for y in range (number_of_laps_around_the_rover):
        primary_slot = 0
        #Each loop is a single Switch in the LED
        for x in range(8):
            slots = [0, 1, 2, 3, 4, 5, 6, 7]
            #Determine the chaser slots
            first_chaser_slot = primary_slot -1
            if first_chaser_slot<0:
                first_chaser_slot += 8
            second_chaser_slot = primary_slot -2
            if second_chaser_slot<0:
                second_chaser_slot+=8
            #set the pixels
            roverLed.strip.setPixelColor(primary_slot, primaryColor)
            roverLed.strip.setPixelColor(first_chaser_slot, chaseColor)
            roverLed.strip.setPixelColor(second_chaser_slot, chaseColor)
            #Wipe the other LEDs
            #Remove from array
            slots.remove(primary_slot)
            slots.remove(first_chaser_slot)
            slots.remove(second_chaser_slot)
            #Loop through the rest of the array and set them to blank
            for empty_slot in slots:
                roverLed.strip.setPixelColor(empty_slot, empty_color)
            roverLed.strip.show()
            time.sleep(.1) 
            #increment the counter
            primary_slot= primary_slot+1
            if primary_slot>7:
                primary_slot=0

def test_ChaseBeginner(primaryColor, chaseColor, number_of_laps_around_the_rover):
    roverLed=Led()   
    empty_color = Color(0, 0, 0) #Empty Color
    #each loop is a lap around the rover
    for y in range (number_of_laps_around_the_rover):
        #Set the first pixel and the chase pixels
        roverLed.strip.setPixelColor(0, primaryColor)
        roverLed.strip.setPixelColor(7, chaseColor)
        roverLed.strip.setPixelColor(6, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(1, empty_color)
        roverLed.strip.setPixelColor(2, empty_color)
        roverLed.strip.setPixelColor(3, empty_color)
        roverLed.strip.setPixelColor(4, empty_color)
        roverLed.strip.setPixelColor(5, empty_color)
        roverLed.strip.show()
        time.sleep(.1) 
        #Slide everything over one
        roverLed.strip.setPixelColor(1, primaryColor)
        roverLed.strip.setPixelColor(0, chaseColor)
        roverLed.strip.setPixelColor(7, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(2, empty_color)
        roverLed.strip.setPixelColor(3, empty_color)
        roverLed.strip.setPixelColor(4, empty_color)
        roverLed.strip.setPixelColor(6, empty_color)
        roverLed.strip.setPixelColor(6, empty_color)
        roverLed.strip.show()
        time.sleep(.1) 
        #Slide everything over one
        roverLed.strip.setPixelColor(2, primaryColor)
        roverLed.strip.setPixelColor(1, chaseColor)
        roverLed.strip.setPixelColor(0, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(3, empty_color)
        roverLed.strip.setPixelColor(4, empty_color)
        roverLed.strip.setPixelColor(5, empty_color)
        roverLed.strip.setPixelColor(6, empty_color)
        roverLed.strip.setPixelColor(7, empty_color)
        roverLed.strip.show()
        time.sleep(.1) 
        #Slide everything over one
        roverLed.strip.setPixelColor(3, primaryColor)
        roverLed.strip.setPixelColor(2, chaseColor)
        roverLed.strip.setPixelColor(1, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(4, empty_color)
        roverLed.strip.setPixelColor(5, empty_color)
        roverLed.strip.setPixelColor(6, empty_color)
        roverLed.strip.setPixelColor(7, empty_color)
        roverLed.strip.setPixelColor(0, empty_color)
        roverLed.strip.show()
        time.sleep(.1) 
        #Slide everything over one
        roverLed.strip.setPixelColor(4, primaryColor)
        roverLed.strip.setPixelColor(3, chaseColor)
        roverLed.strip.setPixelColor(2, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(5, empty_color)
        roverLed.strip.setPixelColor(6, empty_color)
        roverLed.strip.setPixelColor(7, empty_color)
        roverLed.strip.setPixelColor(0, empty_color)
        roverLed.strip.setPixelColor(1, empty_color)
        roverLed.strip.show()
        time.sleep(.1) 
        #Slide everything over one
        roverLed.strip.setPixelColor(5, primaryColor)
        roverLed.strip.setPixelColor(4, chaseColor)
        roverLed.strip.setPixelColor(3, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(6, empty_color)
        roverLed.strip.setPixelColor(7, empty_color)
        roverLed.strip.setPixelColor(0, empty_color)
        roverLed.strip.setPixelColor(1, empty_color)
        roverLed.strip.setPixelColor(2, empty_color)
        roverLed.strip.show()
        time.sleep(.1)
        #Slide everything over one
        roverLed.strip.setPixelColor(6, primaryColor)
        roverLed.strip.setPixelColor(5, chaseColor)
        roverLed.strip.setPixelColor(4, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(7, empty_color)
        roverLed.strip.setPixelColor(0, empty_color)
        roverLed.strip.setPixelColor(1, empty_color)
        roverLed.strip.setPixelColor(2, empty_color)
        roverLed.strip.setPixelColor(3, empty_color)
        roverLed.strip.show()
        time.sleep(.1)
        #Slide everything over one
        roverLed.strip.setPixelColor(7, primaryColor)
        roverLed.strip.setPixelColor(6, chaseColor)
        roverLed.strip.setPixelColor(5, chaseColor) 
        #Set the empty ones  
        roverLed.strip.setPixelColor(0, empty_color)
        roverLed.strip.setPixelColor(1, empty_color)
        roverLed.strip.setPixelColor(2, empty_color)
        roverLed.strip.setPixelColor(3, empty_color)
        roverLed.strip.setPixelColor(4, empty_color)
        roverLed.strip.show()
        time.sleep(.1)
        
from Ultrasonic import *
ultrasonic=Ultrasonic()                
def test_Ultrasonic():
    try:
        while True:
            data=ultrasonic.get_distance()   #Get the value
            print ("Obstacle distance is "+str(data)+"CM")
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")


from Line_Tracking import *
line=Line_Tracking()
def test_Infrared():
    try:
        while True:
            print("IRO1:  "+str(GPIO.input(line.IR01)))
            # print("IRO2:  "+str(GPIO.input(line.IR02)))
            # print("IRO3:  "+str(GPIO.input(line.IR03)))
            if GPIO.input(line.IR01)!=True and GPIO.input(line.IR02)==True and GPIO.input(line.IR03)!=True:
                print ('Middle')
            elif GPIO.input(line.IR01)!=True and GPIO.input(line.IR02)!=True and GPIO.input(line.IR03)==True:
                print ('Right')
            elif GPIO.input(line.IR01)==True and GPIO.input(line.IR02)!=True and GPIO.input(line.IR03)!=True:
                print ('Left')
    except KeyboardInterrupt:
        print ("\nEnd of program")


from servo import *
pwm=Servo()
def test_Servo():
    try:
        while True:
            for i in range(50,110,1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(110,50,-1):
                pwm.setServoPwm('0',i)
                time.sleep(0.01)
            for i in range(80,150,1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)
            for i in range(150,80,-1):
                pwm.setServoPwm('1',i)
                time.sleep(0.01)   
    except KeyboardInterrupt:
        pwm.setServoPwm('0',90)
        pwm.setServoPwm('1',90)
        print ("\nEnd of program")
        
        
from ADC import *
adc=Adc()
def test_Adc():
    try:
        while True:
            Left_IDR=adc.recvADC(0)
            print ("The photoresistor voltage on the left is "+str(Left_IDR)+"V")
            Right_IDR=adc.recvADC(1)
            print ("The photoresistor voltage on the right is "+str(Right_IDR)+"V")
            Power=adc.recvADC(2)
            print ("The battery voltage is "+str(Power*3)+"V")
            time.sleep(1)
            print ('\n')
    except KeyboardInterrupt:
        print ("\nEnd of program")

from Buzzer import *
buzzer=Buzzer()
def test_Buzzer():
    try:
        buzzer.run('1')
        time.sleep(1)
        print ("1S")
        time.sleep(1)
        print ("2S")
        time.sleep(1)
        print ("3S")
        buzzer.run('0')
        print ("\nEnd of program")
    except KeyboardInterrupt:
        buzzer.run('0')
        print ("\nEnd of program")
           
# Main program logic follows:
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 
    if sys.argv[1] == 'Led':
        test_Led()
    elif sys.argv[1] == 'Motor':
        test_Motor()
    elif sys.argv[1] == 'Ultrasonic':
        test_Ultrasonic()
    elif sys.argv[1] == 'Infrared':
        test_Infrared()        
    elif sys.argv[1] == 'Servo': 
        test_Servo()               
    elif sys.argv[1] == 'ADC':   
        test_Adc()  
    elif sys.argv[1] == 'Buzzer':   
        test_Buzzer() 
    elif sys.argv[1] == 'Chase':
        primaryColor = Color(128,0,128) #Purple
        chaseColor = Color(255,255,0) #Yellow
        test_ChaseLeds(primaryColor, chaseColor, 10)
    elif sys.argv[1] == 'Chase Beginner':
        primaryColor = Color(128,0,128) #Purple
        chaseColor = Color(255,255,0) #Yellow
        test_ChaseBeginner(primaryColor, chaseColor, 10)
    else:
        print("Not a valid test case.")
        exit() 

        
        
        
        

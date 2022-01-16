import time
from PCA9685 import PCA9685
class JohnyMotor:
    def __init__(self):
        self.pwm = PCA9685(0x40, debug=True)
        self.pwm.setPWMFreq(50)
        #Attr to tell the motor whether values need to be reversed or not
        self.need_to_reverse = True
        
    def set_Left_Upper_Wheel(self,speed: int):
        """This method will set the left lower wheel with the speed provided

        Args:
            speed (int): This is an integer value that has to be within the range of -4095 and 4095
        """
        #Method to ensure that the values are within range and
        #convert them if the motor is wired backwards
        speed = self.__sanitize_motor_value(speed)
        if speed>0:
            self.pwm.setMotorPwm(0,0)
            self.pwm.setMotorPwm(1,speed)
        elif speed<0:
            self.pwm.setMotorPwm(1,0)
            self.pwm.setMotorPwm(0,abs(speed))
        else:
            self.pwm.setMotorPwm(0,4095)
            self.pwm.setMotorPwm(1,4095)

    def set_Left_Lower_Wheel(self,speed:int):
        """This method will set the left lower wheel with the speed provided

        Args:
            speed (int): This is an integer value that has to be within the range of -4095 and 4095
        """
        #Method to ensure that the values are within range and
        #convert them if the motor is wired backwards
        speed = self.__sanitize_motor_value(speed)
        if speed>0:
            self.pwm.setMotorPwm(3,0)
            self.pwm.setMotorPwm(2,speed)
        elif speed<0:
            self.pwm.setMotorPwm(2,0)
            self.pwm.setMotorPwm(3,abs(speed))
        else:
            self.pwm.setMotorPwm(2,4095)
            self.pwm.setMotorPwm(3,4095)

    def set_Right_Upper_Wheel(self,speed:int):
        """This method will set the right upper wheel with the speed provided

        Args:
            speed (int): This is an integer value that has to be within the range of -4095 and 4095
        """
        #Method to ensure that the values are within range and
        #convert them if the motor is wired backwards
        speed = self.__sanitize_motor_value(speed)
        if speed>0:
            self.pwm.setMotorPwm(6,0)
            self.pwm.setMotorPwm(7,speed)
        elif speed<0:
            self.pwm.setMotorPwm(7,0)
            self.pwm.setMotorPwm(6,abs(speed))
        else:
            self.pwm.setMotorPwm(6,4095)
            self.pwm.setMotorPwm(7,4095)

    def set_Right_Lower_Wheel(self,speed:int):
        """This method will set the right lower wheel with the speed provided

        Args:
            speed (int): This is an integer value that has to be within the range of -4095 and 4095
        """
        #Method to ensure that the values are within range and
        #convert them if the motor is wired backwards
        speed = self.__sanitize_motor_value(speed)
        if speed>0:
            self.pwm.setMotorPwm(4,0)
            self.pwm.setMotorPwm(5,speed)
        elif speed<0:
            self.pwm.setMotorPwm(5,0)
            self.pwm.setMotorPwm(4,abs(speed))
        else:
            self.pwm.setMotorPwm(4,4095)
            self.pwm.setMotorPwm(5,4095)
 
    def set_all_motors(self,left_upper:int, left_lower:int, right_upper:int, right_lower:int):
        """[summary]

        Args:
            left_upper (int): This is an integer value that has to be within the range of -4095 and 4095
            left_lower (int): This is an integer value that has to be within the range of -4095 and 4095
            right_upper (int): This is an integer value that has to be within the range of -4095 and 4095
            right_lower (int): This is an integer value that has to be within the range of -4095 and 4095
        """
        self.set_Left_Upper_Wheel(left_upper)
        self.set_Left_Lower_Wheel(left_lower)
        self.set_Right_Upper_Wheel(right_upper)
        self.set_Right_Lower_Wheel(right_lower)

    def __sanitize_motor_value(self,value):
        if self.need_to_reverse:
            value = -value
        if value>4095:
            return 4095
        elif value<-4095:
            return -4095 
        return value 
            
            
PWM=JohnyMotor()          
def run_through_capabilities(): 
    PWM.set_all_motors(2000,2000,2000,2000)       #Forward
    time.sleep(1)
    PWM.set_all_motors(0,0,0,0)       #STOP
    PWM.set_all_motors(-2000,-2000,-2000,-2000)   #Back
    time.sleep(1)
    PWM.set_all_motors(0,0,0,0)       #STOP
    PWM.set_all_motors(-500,-500,2000,2000)       #Left 
    time.sleep(1)
    PWM.set_all_motors(0,0,0,0)       #STOP
    PWM.set_all_motors(2000,2000,-500,-500)       #Right    
    time.sleep(1)
    PWM.set_all_motors(0,0,0,0)                   #Stop

    
def destroy():
    PWM.set_all_motors(0,0,0,0)                   
if __name__=='__main__':
    try:
        run_through_capabilities()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

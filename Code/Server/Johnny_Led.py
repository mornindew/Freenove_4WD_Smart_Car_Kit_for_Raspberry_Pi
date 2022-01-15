from Led import Led
from rpi_ws281x import *
import random
import time

class JohnnyLed(Led):

    def display_led(self,index,R,G,B):
        """I wrote this to display LED.  I found it to be much simpler than 
        the stuff that came with the library

        Args:
            index ([int]): [This is the integer value representing the slot in for the LED]
            R ([int]): [This is the 256 (0-255) integer value that represents its red color]
            G ([int]): [This is the 256 (0-255) integer value that represents its green color]
            B ([int]): [This is the 256 (0-255) integer value that represents its blue color]
        """
        color=self.LED_TYPR(self.ORDER,Color(R,G,B))
        self.strip.setPixelColor(index,color)
        self.strip.show()

    def random_led_display(self, number_of_intervals):
        for x in range(number_of_intervals):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            #randomly choose 3 
            for x in range (3):
                slot_to_choose = random.randint(0,7)
                self.strip.setPixelColor(slot_to_choose, Color(red, green, blue))
                self.strip.show()
                time.sleep(.01)     

    def chase_color_around(self, primaryColor, chaseColor, number_of_cycles):
        empty_color = Color(0, 0, 0)
        primary_slot = 0
        for x in range(number_of_cycles):
            slots = [0, 1, 2, 3, 4, 5, 6, 7]
            #Determine the chaser slots
            first_chaser_slot = primary_slot -1
            if first_chaser_slot<0:
                first_chaser_slot += 8
            second_chaser_slot = primary_slot -2
            if second_chaser_slot<0:
                second_chaser_slot+=8
            #set the pixels
            self.strip.setPixelColor(primary_slot, primaryColor)
            self.strip.setPixelColor(first_chaser_slot, chaseColor)
            self.strip.setPixelColor(second_chaser_slot, chaseColor)
            #Wipe the other LEDs
            #Remove from array
            slots.remove(primary_slot)
            slots.remove(first_chaser_slot)
            slots.remove(second_chaser_slot)
            #Loop through the rest of the array and set them to blank
            for empty_slot in slots:
                self.strip.setPixelColor(empty_slot, empty_color)
            self.strip.show()
            time.sleep(.1) 
            #increment the counter
            primary_slot= primary_slot+1
            if primary_slot>7:
                primary_slot=0





        
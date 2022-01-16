# Jr Robotics Club

This is the loose curriculum (emphasis on loose) for the rover build.   It is intended to layout the topics that we will cover and missions for each week.

# Missions

Below are the missions and the topic areas for each mission.

## Mission 1 - Hardware Build
This mission is to build the actual rover and it's hardware.  Ideally by the end of this mission we will have a fully formed rover and all the components are installed

## Mission 2 - Setup Development Environment
This mission is to ensure that everyone has their development environment setup and can connect to the rover.
### Topics

 1. Connect over VNC
 2. Browse Linux
 3. Open python file in editor
 4. (Optional) Setup VS Code over SSH

## Mission 3 - Module Test
This mission is to test each of the components of the Rover and iron out any issues that happened in the build.

### Topics

 - Run code from command line
 - reverse motors (if needed)
 - Test all modules

## Mission 4 - Start Coding
The goal of this mission is to start getting familiar with coding and how code works.  We will start by pulling apart the Motor code and  walking through in detail.

### Mission Challenge
Write code to have your rover solve a maze.  The dimensions of the maze will be 4 feet forward --> right turn 90 degrees --> 2 feet forward --> left turn 90 degrees --> 2 feet forward --> left turn 90 degrees --> 3 feet forward --> right turn 90 degrees --> forward 1 foot --> 360 and stop

Extra Credit - For extra credit you can make the LED's on the rover show green when moving forward, yellow when turning, and red when stopping

### Topics

 - Explain Code Organization 
	 - Libraries
	 - Methods
	 - Functions
	 - Classes
 - Explain How Languages Work
 - Show what a computer "sees"

## Mission 5 - Code the LED
The goal of this mission is to become familiar with the LED code and how it works.  We will pull apart the LED code and better understand how it works.

### Mission Challenge
Write a custom LED sequence that will "chase" and LED around the rover.   The primary light will be chased by two other lights (e.g. red will be chased by two green lights).  Every time that the red moves to the next spot then the green lights will also move.

### Topics

 - Explain LED and RGB color scheme
 - Explain looping
 - Explain the LED Slots and how GPIO works
 - Show the horrible code that freenove gave us

### Example function for cleaner LED
``
def  display_led(self, index, R, G, B):
	self.strip.setPixelColor(index, Color(R, G, B))
	self.strip.show()
``

## Mission 6 - Name your rover
This mission is to move out of running things in the test classes and actually create a class to represent your rover.

### Topics

 - Explain Object Oriented 
 - Explain Classes
 - Explain methods and functions (in more detail)
 - Explain the init methods
 - Explain the input message

### Mission Challenge
Create a custom Class for your rover that will prompt the user to let the user control it from the command line.  The user will be asked a direction and a duration.

 ## Mission 7 - TBD
[Description of the Mission]

### Topics
 - [List of topics]

### Mission Challenge
[Description of challenge]

 ## Mission 8 - TBD
[Description of the Mission]

### Topics
 - [List of topics]

### Mission Challenge
[Description of challenge]

 ## Mission 9 - TBD
[Description of the Mission]

### Topics
 - [List of topics]

### Mission Challenge
[Description of challenge]

 ## Mission 10 - TBD
[Description of the Mission]

### Topics
 - [List of topics]

### Mission Challenge
[Description of challenge]


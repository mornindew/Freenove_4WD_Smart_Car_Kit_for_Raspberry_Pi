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
 - Explain the specifics of the command 
	- sudo, python, test.py Motor	

## Mission 4 - Start Coding
The goal of this mission is to start getting familiar with coding and how code works.  We will start by pulling apart the Motor code and  walking through in detail.

### Mission Challenge
Write code to have your rover solve a maze.  The dimensions of the maze will be 4 feet forward --> right turn 90 degrees --> 2 feet forward --> left turn 90 degrees --> 2 feet forward --> left turn 90 degrees --> 3 feet forward --> right turn 90 degrees --> forward 1 foot --> 360 and stop

Extra Credit - For extra credit you can make the LED's on the rover show green when moving forward, yellow when turning, and red when stopping

<img src='Picture/maze.jpg' width='50%'/>


Solving the Maze: 

<img src='Picture/mission4.gif' width='25%'/>


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
Write a custom LED sequence that will "chase" an LED around the rover 10 times (not 10 LEDs, 10 times around the rover).   The primary light will be chased by two other lights (e.g. red will be chased by two green lights).  Every time that the red moves to the next spot then the green lights will also move.

Break this mission into two parts:
 - Part One - do the mission with a single loop.  One loop per revolution around the car
 - Part Two - Do this mission with an embedded loop.   A loop for a revolution and then a loop within it to iterate the lights

#### Hints
 - Every LED is in one of three states at all times (primary color, chase color, or off)
 - multiple changes can be made to the leds before "showing them"
 - Give a time gap between the light rotations or it will happen too fast
 - Loops are your friend
 - Each LED Slot is a numeric value and loops count in numbers - use this to your advantage
 - Expert Level Hint - Learn About Arrays and see if you can use an Array of Integers (representing your LED slot) to your advantage

<img src='Picture/mission5.gif' width='25%'/>

Solving the LED Chase: 

 - Solving with only one loop - https://github.com/mornindew/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/blob/1d4159dec9ba505444f4ca2b9858b46fb2e943ae/Code/Server/test.py#L166-L266
 - Solving with nested loops - https://github.com/mornindew/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/blob/1d4159dec9ba505444f4ca2b9858b46fb2e943ae/Code/Server/test.py#L132-L164 



### Topics

 - Explain LED and RGB color scheme
 - Explain LED Slots
 - Explain IF Statements
 - Explain looping
 - Explain parameters
 - Show creating a new function
 - Discuss getting away from copying code

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


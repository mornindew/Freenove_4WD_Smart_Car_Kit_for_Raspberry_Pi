#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)
print(gamepad.capabilities(verbose=True))
#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():

    if event.type == ecodes.EV_KEY:
    #print(categorize(event))
        keyEvent = categorize(event)
        print(keyEvent)
        # print("####")
    elif event.type == ecodes.BTN_GAMEPAD:
        print("GAMEPAD")
    elif event.type == ecodes.EV_ABS:
      if ecodes.ABS[event.code] == 'ABS_Y':
        # if event.value == 0:
        #   print("UP")
        # elif event.value == 255:
        #   print("DOWN")
        # else:
        #   print(event.value)
        #   print("release")
        print("Y VALUE: "+str(event.value))
      elif ecodes.ABS[event.code] == 'ABS_X':
        print("X VALUE: "+str(event.value))
      elif event.code == 16:
        print("[inputs]", event.code, event.value)
        if event.value == -1: # UP
            print("LEFT")
            #func.lift("UP", robot)
        elif event.value == 1: # DOWN
            print("RIGHT")
            #func.lift("DOWN", robot)
        else:
            print("REleASE")
            #robot.motors.set_lift_motor(0)
      elif event.code == 17: # DPAD
        print("[inputs]", event.code, event.value)
        if event.value == -1: # UP
            print("UP")
            #func.lift("UP", robot)
        elif event.value == 1: # DOWN
            print("DOWN")
            #func.lift("DOWN", robot)
        else:
            print("REleASE")
            #robot.motors.set_lift_motor(0)
      else:
        print(event.code)
        if event.value == 0:
          print("LEFT")
        elif event.value == 255:
          print("RIGHT")
        else:
          print(event.value)
          print("release")
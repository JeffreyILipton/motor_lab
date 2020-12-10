import board
import digitalio
import time

#print('stepper functions')
#connect LED light
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Connect step and direction pins
step_pin = digitalio.DigitalInOut(board.D27)
step_pin.direction = digitalio.Direction.OUTPUT
dir_pin = digitalio.DigitalInOut(board.D17)
dir_pin.direction = digitalio.Direction.OUTPUT

#Connect limit switches
button = digitalio.DigitalInOut(board.D22)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
 
button2 = digitalio.DigitalInOut(board.D4)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP


def step():
    ''' flip the value of the step pin to take a step'''
    step_pin.value = not (step_pin.value)


def steps(N,delay):
    '''take N steps with delay seconds in between them'''
    for i in range(N):
        step()
        time.sleep(delay)
        
def move_to(dist):
    dir_pin.value = False # turn cw
    #reset to the left side
    while button.value!=1:
        steps(1,0.003) # rotate the motor a little bit
    dir_pin.value = True # turn ccw
    for x in range(dist):
        steps(1,0.003) # rotate the motor a little bit
        if button2.value ==1:
            break
            
def toggle_LED(switch):
    if switch==1:
        led.value = True #turn on LED
    if switch==0:
        led.value = False #turn off LED
    
           
'''
while True:
    command=int(input('what should the motor do? 0,1 for light int=dist'))
    try:
        if command==0:
            toggle_LED(False)
        elif command==1:
            toggle_LED(True)
        else:
            move_to(command)
    except:
        print('incorrect instruction')
'''  

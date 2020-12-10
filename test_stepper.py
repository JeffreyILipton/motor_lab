import board
import digitalio
import time

print('running stepper')
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

print("running stepper")
def step():
    ''' flip the value of the step pin to take a step'''
    step_pin.value = not (step_pin.value)


def steps(N,delay):
    '''take N steps with delay seconds in between them'''
    for i in range(N):
        step()
        time.sleep(delay)

while True:
    steps(1,0.003) # rotate the motor a little bit
    if button.value==1:
        dir_pin.value = True # turn ccw
        led.value = True #turn on LED
    if button2.value ==1:
        dir_pin.value = False # turn cw
        led.value = False #tunr on LED
  

import time
import board
import pulseio
import digitalio
 
# Initialize PWM output for the servo (on pin D5):
servo = pulseio.PWMOut(board.D5, frequency=50)

#connect LED light
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

print("running servo")
 
# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle
 
def move_to(dist):
    servo.duty_cycle = servo_duty_cycle(dist/100)
 
def toggle_LED(switch):
    if switch==1:
        led.value = True #turn on LED
    if switch==0:
        led.value = False #turn off LED
 
 
 
'''
# Main loop will run forever moving between 1.0 and 2.0 mS long pulses:
while True:

    duty=float(input('where should the motor go?'))
    led.value = True #turn on LED
    servo.duty_cycle = servo_duty_cycle(duty)
    time.sleep(2)
    led.value = False #tunr on LED
'''
    
    
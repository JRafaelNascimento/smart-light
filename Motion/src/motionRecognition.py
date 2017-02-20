import Adafruit_BBIO.GPIO as GPIO
import time
 
#create a variable called PIR, which refers to the P8_11 pin
PIR = "P8_19"
 
#initialize the pin as an INPUT
GPIO.setup(PIR, GPIO.IN)

#loop forever
print "Start"
while True:
    #sends an email when motion has been detected
    if GPIO.input(PIR):
        print("Motion Detected")
    else:
        print("No Motion Detected")
    time.sleep(2) 
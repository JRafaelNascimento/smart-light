import Adafruit_BBIO.GPIO as GPIO
import time
 
#create a variable called PIR, which refers to the P8_11 pin
PIR = "P8_19"
LED = "P8_17"
 
#initialize the pin as an INPUT
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

#loop forever
while True:
    #sends an email when motion has been detected
    if GPIO.input(PIR):
        GPIO.output(LED, GPIO.HIGH)
        print("Motion Detected")
    else:
        GPIO.output(LED, GPIO.LOW)
        print("No Motion Detected")
    time.sleep(2) 
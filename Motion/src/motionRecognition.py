import Adafruit_BBIO.GPIO as GPIO
import time
 
#create a variable called PIR, which refers to the P8_11 pin
PIR = "P8_11"
led = "P8_13";
 
#initialize the pin as an INPUT
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.add_event_detect(PIR, GPIO.RISING)

while True:
    #sends an email when motion has been detected
    if GPIO.event_detected(PIR):
        GPIO.output(led, GPIO.HIGH) 
    else:
    	GPIO.output(led, GPIO.LOW)
    time.sleep(0.05) #loop every 50 miliseconds to not overburden the CPU
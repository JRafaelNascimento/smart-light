import subprocess
import Adafruit_BBIO.GPIO as GPIO
import time
 
#create a variables to PINS
PIR = "P8_19"
LIGHT = "P8_17"
 
#initialize the pin as IN or OUT
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LIGHT, GPIO.OUT)

#Variables used on system for control
motion = False
lightPriority = False

#Running the process of phoenixsphinx and getting the output
proc = subprocess.Popen(['sh', '-c', 'pocketsphinx_continuous -adcdev hw:1,0  -nfft 2048 -samprate 48000 -lm'],stdout=subprocess.PIPE)

#Method that process the string recognized by microfone
def runstring(text):
    #Turning on light if user says 'lights on'
    if (text == "light on"):
        GPIO.output(LIGHT, GPIO.HIGH)
        lightPriority = True
    #Turning off light if user says 'lights off'
    elif (text == "light off"):
        GPIO.output(LIGHT, GPIO.LOW)
        lightPriority = True
    #Turning on motion if user says 'lights on'
    elif (text == "motion on"):
        motion == True
    #Turning off motion if user says 'lights off'
    elif (text == "motion off"):
        motion == False
    else:
        print "Unrecognized word"
    
#Infinite loop
while True:
    #Checking the string recognized by the microfone
    line = proc.stdout.readline()
    if line != '':
        #Getting the output string generated by phoenixsphinx process
        output = line.rstrip()
        #print output
        if (len(output.split("READY"))>1):
            print "Speak"
        if (len(output.split("please wait"))>1):
            print "Please wait"
        if (len(output.split(":"))>1):
            runstring(str(output.split(":")[1]))

    #Checking if user wants that light turns on with motion and checking PIR
    if GPIO.input(PIR) && motion == True && lightPriority == False:
        GPIO.output(LIGHT, GPIO.HIGH)
        print("Motion Detected")
    elif !GPIO.input(PIR):
        GPIO.output(LIGHT, GPIO.LOW)
        print("No Motion Detected")
        lightPriority = False
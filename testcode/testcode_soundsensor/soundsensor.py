import RPi.GPIO as GPIO
import time

#GPIO SETUP
sound = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)
def callback(sound):
        if GPIO.input(sound):
		       print ("sound here")
	    else:
               print ("Sound here!")

GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=1000)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    time.sleep(1000)

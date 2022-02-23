import RPi.GPIO as GPIO
import time

sensor = 16
buzzer = 18

def ultrasonic():
	  	
		                          
		GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

		TRIG = 23                                  #Associate pin 23 to TRIG
		ECHO = 24                                  #Associate pin 24 to ECHO

		print ("Distance measurement in progress")

		GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
		GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

		while True:

		  GPIO.output(TRIG, False)                 #Set TRIG as LOW
		  print ("Waitng For Sensor To Settle")
		  time.sleep(2)                            #Delay of 2 seconds

		  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
		  time.sleep(0.00001)                      #Delay of 0.00001 seconds
		  GPIO.output(TRIG, False)                 #Set TRIG as LOW

		  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
		    pulse_start = time.time()              #Saves the last known time of LOW pulse

		  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
		    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

		  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

		  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
		  distance = round(distance, 2)            #Round to two decimal points

		  if distance > 2 and distance < 400:      #Check whether the distance is within range
		    print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
		  else:
		    print ("Out Of Range") 
		    
		    ultrasonic();                  #display out of range
	  
  
def proximity():
  
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
	GPIO.setup(3, GPIO.OUT)         #LED output pin
	while True:
		i=GPIO.input(11)
	if i==0:                 #When output from motion sensor is LOW
		print ("No intruders",i)
		GPIO.output(3, 0)  #Turn OFF LED
		time.sleep(0.1)
	elif i==1: 
	
		proximity();     
  
def infra_red():
  
	

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(sensor,GPIO.IN)
	GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("IR Sensor Ready.....")
print (" ")

try: 
	while True:
		if GPIO.input(sensor):
			GPIO.output(buzzer,True)
			print ("Object Detected")
			while GPIO.input(sensor):
				time.sleep(0.2)
			else:
				GPIO.output(buzzer,False)


except KeyboardInterrupt:
	GPIO.cleanup()
	infra_red();
  

 

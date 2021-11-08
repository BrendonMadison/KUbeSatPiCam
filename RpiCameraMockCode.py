#RPi camera mock code for taking a still image and then processing with the petri dish code
#Written by Brendon Madison on 2nd October 2021

from picamera import PiCamera
from time import sleep
import time
import os

camera = PiCamera()

#time between each image
delay_time = 0.5*60

#time images are taken, below is 48 hours
camera_time = (60*48*60.0)

sleep(5)

#Take pictures for 48 hours
for i in range(int(camera_time/delay_time) + 1):
    #filename = str('LabTest%s.jpg' % i)
    filename = str(str(int(time.time()))+'.jpg')
    camera.resolution = (1280,720)
    camera.capture(filename)
    
    
    #sleep for 10 seconds to ensure the image is saved correctly before the processing script is called
    sleep(10)
    
    print("Captured: " + filename)
    #Calls the processor code "FindPetriDish.py"
    os.system(str('python3 FindPetriDish.py ') + str(filename))
    
    #sleep for 60 seconds to ensure the above code is run with no 
    sleep(60)
    
    #sleep for (delay_time) seconds . Default is 5 minutes
    sleep(delay_time)

camera.close()

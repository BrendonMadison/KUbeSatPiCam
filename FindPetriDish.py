#Purpose: To find petri dishes in the image (treated as circles) and then find the  pixel luminosity (integral of the rgb values) to use as a characteristic of petri dish growth

#Code Requirements: Requires python3 , and the cv2, numpy, argparse libraries. 

#User requirements: User must pass an argument to this code when this code is called. Particularly this argument must be a string that is equal to the name of the image to be processed.
#Example that you would use in terminal: python3 FindPetriDish.py MyPetriDishPhoto.jpg

#Outputs: This code outputs an image with the petri dishes labelled with their circles as well as text that says what order the algorithm identified the petri dishes
#It also reports the pixel luminosity integrated over the entire petri dish.

#Author: Written by Brendon Madison, grad student of KU PHSX and ASTR on 2nd of October, 2021

import cv2
import numpy as np
import argparse
import time

parser = argparse.ArgumentParser(description='Find petri dishes and integrate their luminosity (rgb values).')
parser.add_argument('Im',metavar='Im',type=str,help='String for name of image')
args = parser.parse_args()

image = cv2.imread(args.Im)
output = image.copy()
img = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 100,minRadius=190,maxRadius=210)

CirclesColor = []
CirclesRad = []
h = output.shape[0]
w = output.shape[1]

# If some circle is found
if circles is not None:
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   #print(circles)
   index = 0
   for i in circles:
    CirclesColor.append(0)
    CirclesRad.append(0)
   # loop over the circles
   for x in range(w):
        for y in range(h):
            for i in range(len(circles)):
                CirclesRad[i] = circles[i][2]
                if np.sqrt((circles[i][0] - x)**2 + (circles[i][1] - y)**2) < circles[i][2]:
                    CirclesColor[i] += np.sum(image[y,x])
   for (x, y, r) in circles:
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
      cv2.putText(output,str('Index:')+str(index), (x,y+15), cv2.FONT_HERSHEY_PLAIN, 1.0, (20,20,20),4)
      cv2.putText(output,str('Lumi:')+str(CirclesColor[index]), (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (20,20,20),4)
      cv2.putText(output,str('Index:')+str(index), (x,y+15), cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255),1)
      cv2.putText(output,str('Lumi:')+str(CirclesColor[index]), (x,y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255),1)
      index += 1
print(str(time.time())+"\t"+str(CirclesRad)+"\t"+str(CirclesColor))
#print(CirclesColor)
# show the output image
#cv2.imshow(str(args.Im[0:len(args.Im)-4])+str('Circles.png'),output)
cv2.waitKey(0)
cv2.imwrite(str(args.Im[0:len(args.Im)-4])+str('Circles.png'),output) 

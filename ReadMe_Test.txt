To test the FindPetriDish.py code two stock images of cultures on petri dishes were used.

UPDATE: As of end of October 2021 successful tests were conducted in Dr. Ben Sike's Biology/Mycology lab using actual fungal samples

They are called "SikesLabExample.jpg" and "SikesLabExampleCircles.jpg" .

In these images the top center petri dish has been replaced with still images of a video of culture growth in a petri dish.

Note that, in order to get the code to work well, you need to change the "minRadius" and "maxRadius" of the circle finding algorithm to be similar to the pixel radius you expect for your image(s).

Results:
1.) The algorithm was able to find the petri dishes, and nothing else, across both images. So this is part is a success.

2.) The pixel luminosity values do seem to correlate with culture growth in the stock image cultures and, in the case of the two still petri dishes, they do indeed increase in the older, second, more growth, image. (Other images that confirm this were not included)


To do?:

0.) Test RPiCameraMockCode.py for use with FindPetriDish.py [DONE]

1.) Have a text output that orders these luminosity values in terms of the x,y of the circles so that the x,y values can be used to ensure that each luminosity value corresponds to the correct petri dish. [DONE but then reverted]

2.) Test this with a live sequence of images taken with a still camera and petri dish(es). Since this is a python script it can be done through an Raspberry Pi using an RPi camera (which can also run in a python script). [DONE]

3.) With 2.) also adding in a time component and then a corresponding change in pixel luminosity per change in unit time, essentially a time differential of pixel luminosity. Then test to see if this correlates with the area/surface growth rate of the culture.

4.) Try to downsize the images and repeat this algorithm as, for a space mission, you likely wouldn't be able to downlink lots of large image files.

Requirements:

1.) Download cv2. On RPi this requires installing cv2 using "sudo python3 -m pip install opencv-python" or installing pip3 and using it.
	a.) cv2 requires that you update to the newest version of numpy (>1.8) using "pip install -U numpy"
	b.) cv2 requires that you download libatlas using "sudo apt-get install libatlas-base-dev". For some reason pip doesn't do this automatically though normally it would...
	

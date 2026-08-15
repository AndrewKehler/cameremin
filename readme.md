# This is the official release of the Cameremin.
## To install and run
Please check the releases and download the .zip file. This includes all the source code in a simple .exe file.
Ensure you have a connected camera to your device, and a working audio output. Simply run the camera.exe. The window will open both the camera window, and the Max executable. Once two hands are detected in frame, the sound starts. 

## If you are running it off the source code
You must ensure you have all packages installed in Python311. Run the main.py file and the theremin.maxpat file.

## To play
The right hand controls pitch and vibrato. Follow the marked guidelines for pitch. The pitch is decided by the placement of the thumb. Increase the distance between index and thumb to increase vibrato speed. Do the opposite to decrease vibrato. 

The left hand controls volume, where a small distance between fingers is a louder volume. A larger increase in distance is a quieter volume. This counteracts the depth issue at the cost of some intuition.

## To close
Press 'q' to close the camera window. This will not close the Max executable. Pressing 'Ctrl + Q' will close the Max executable. If the camera is open when Max is closed, this will also terminate the camera window.

## For more information
See the paper within the release or within the source code for details on the inner workings.

from client import *
import numpy as np
import cv2
import mediapipe as mp
import math

capt = cv2.VideoCapture(0)
#capture resolution constants
WIDTH = int(capt.get(3) *1.5)
HEIGHT = int(capt.get(4)*1.5)
#accesses the mediapipe library
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
connections = [(0,5),(5,9),(9,13),(13,17),(17,0),(8,4)]
hands = mp_hands.Hands()

#Draw the guidelines based off the scaled frequency values in MAX/MSP.
def draw_guidelines(frame):
    #position along the X axis that the guidelines should start or end
    X_DIST_START = 10
    X_DIST_END = 500
    #font size
    FONT = 0.5
    
    COLOR = (0,255,0)

    frame = cv2.line(frame, (X_DIST_START, 0), (X_DIST_START, 1000), COLOR, thickness=4)
    
    frame = cv2.line(frame, (X_DIST_START, 680), (X_DIST_END, 680), COLOR, thickness=4)
    frame = cv2.putText(frame, "A4", org=(X_DIST_END+4,690),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 655), (X_DIST_END, 655), COLOR, thickness=4)
    frame = cv2.putText(frame, "B4", org=(X_DIST_END+4,660),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 635), (X_DIST_END, 635), COLOR, thickness=4)
    frame = cv2.putText(frame, "C5", org=(X_DIST_END+4,635),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 610), (X_DIST_END, 610), COLOR, thickness=4)
    frame = cv2.putText(frame, "D5", org=(X_DIST_END+4,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 575), (X_DIST_END, 575), COLOR, thickness=4)
    frame = cv2.putText(frame, "E5", org=(X_DIST_END+4,585),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 550), (X_DIST_END, 550), COLOR, thickness=4)
    frame = cv2.putText(frame, "F5", org=(X_DIST_END+4,555),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 510), (X_DIST_END, 510), COLOR, thickness=4)
    frame = cv2.putText(frame, "G5", org=(X_DIST_END+4,515),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 460), (X_DIST_END, 460), COLOR, thickness=4)
    frame = cv2.putText(frame, "A5", org=(X_DIST_END+4,465),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 400), (X_DIST_END, 400), COLOR, thickness=4)
    frame = cv2.putText(frame, "B5", org=(X_DIST_END+4,405),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 370), (X_DIST_END, 370), COLOR, thickness=4)
    frame = cv2.putText(frame, "C6", org=(X_DIST_END+4,375),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 310), (X_DIST_END, 310), COLOR, thickness=4)
    frame = cv2.putText(frame, "D6", org=(X_DIST_END+4,315),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 230), (X_DIST_END, 230), COLOR, thickness=4)
    frame = cv2.putText(frame, "E6", org=(X_DIST_END+4,235),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 190), (X_DIST_END, 190), COLOR, thickness=4)
    frame = cv2.putText(frame, "F6", org=(X_DIST_END+4,195),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 110), (X_DIST_END, 110), COLOR, thickness=4)
    frame = cv2.putText(frame, "G6", org=(X_DIST_END+4,115),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    frame = cv2.line(frame, (X_DIST_START, 30), (X_DIST_END, 30), COLOR, thickness=4)
    frame = cv2.putText(frame, "A6", org=(X_DIST_END+4,35),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=FONT,color=COLOR, thickness=2)
    
    return frame

#infinite loop of photos begin taken from the camera. video.
while(capt.isOpened()):
    success, frame = capt.read()
    if success:
        #converts the current frams colours from RBG, to RGB for compatibility with mediapipe.
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(RGB_frame)
        if result.multi_hand_landmarks:
            leftDistance = 0.0
            rightDistance = 0.0
            thumbLeftY = 0.0
            #if it detects 2 hands
            if (len(result.multi_handedness) == 2):
                for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
                    #assumes the camera read is flipped before identifying hands, so left and right are swapped here.
                    label = handedness.classification[0].label
                    if label == "Left":
                        indexRight = hand_landmarks.landmark[8]
                        thumbRight = hand_landmarks.landmark[4]
                        #Pythagoras' theorem with displacement of X and Y.
                        rightDistance = math.sqrt((thumbRight.x - indexRight.x)**2 + (thumbRight.y - indexRight.y)**2)
                    elif(label == "Right"):
                        indexLeft = hand_landmarks.landmark[8]
                        thumbLeft = hand_landmarks.landmark[4]
                        thumbLeftY = thumbLeft.y
                        leftDistance = math.sqrt((thumbLeft.x - indexLeft.x)**2 + (thumbLeft.y - indexLeft.y)**2)

                vals = [thumbLeftY, leftDistance, rightDistance]
                #Sends the values to be converted into OSc and then sent over UDP.
                send(vals)
            else:
                vals = [0.0,0.0,0.5]
                send(vals)
            #Iterates through each handmark and draws it with mediapipe
            for num, marks in enumerate(result.multi_hand_landmarks):
                mp_drawing.draw_landmarks(frame, marks, connections)

        #openCV customizations.
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (WIDTH, HEIGHT))
        draw_guidelines(frame)
        
        cv2.imshow("Theremin", frame)
    #when q is pressed, close the window and break the loop.
    if(cv2.waitKey(1)== ord("q")):
        break
cv2.destroyAllWindows
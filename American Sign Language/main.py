import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time
import math

cap=cv2.VideoCapture(0)
detecter = HandDetector(maxHands=1)

offset = 20
imgsize = 300

counter =0
folder ="data/a"

while True:
    success , img = cap.read()
  


    #img = cv2.resize(img, (800,600), interpolation=cv2.INTER_AREA)
    hands , img = detecter.findHands(img)
    
    if hands :
        hand = hands[0]
        x,y,w,h = hand['bbox']
        
        imgWhite = np.ones((imgsize,imgsize,3),np.uint8 )*255
        
        imgCrop = img[y - offset :y+h+offset,x - offset:x+w+offset]
        
        imgCshape=imgCrop.shape
        
       
        if (h>w):
            w1=(imgsize*w)/h
            w1= math.ceil(w1)
            imgRS=cv2.resize(imgCrop, (w1,imgsize))
            a=math.ceil((imgsize-w1)/2)
            imgWhite[:, a : a+w1] = imgRS
        else:
            h1=math.ceil((imgsize*h)/w)
            imgRS=cv2.resize(imgCrop,(imgsize,h1))
            a=math.ceil((imgsize-h1)/2)
            imgWhite[a:a+h1,:] = imgRS
            
    
       
        
        cv2.imshow('ImageCrop',imgCrop)
        cv2.imshow('white',imgWhite)
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k == ord('s'):
        counter+=1
        cv2.imwrite(f'{folder}/image_{time.time()}.jpg',imgWhite)
        print(counter)
        
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 



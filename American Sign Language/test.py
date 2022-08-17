import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import tensorflow
import math

cap=cv2.VideoCapture(0)
detecter = HandDetector(maxHands=1)
classifier = Classifier("model/keras_model.h5", "model/labels.txt")

offset = 20
imgsize = 300
labels = ["A", "B", "C"]


       
        
        
 
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
            pred, index = classifier.getPrediction(imgWhite,draw =False)
            #print(pred, index)
            cv2.putText(img, labels[index], (x+ math.ceil(w1/2), y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        else:
            h1=math.ceil((imgsize*h)/w)
            imgRS=cv2.resize(imgCrop,(imgsize,h1))
            a=math.ceil((imgsize-h1)/2)
            imgWhite[a:a+h1,:] = imgRS
            pred, index = classifier.getPrediction(imgWhite,draw =False)
            cv2.putText(img, labels[index], (x+ math.ceil(w/2), y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        
        
        #cv2.rectangle(img, (x-offset, y-offset),(x + w+offset, y + h+offset), (255, 0, 255), 4)
            
       
       
        
        cv2.imshow('ImageCrop',imgCrop)
        cv2.imshow('white',imgWhite)
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
   
        
    if k == ord('q'):
       break
   
cap.release()
cv2.destroyAllWindows() 


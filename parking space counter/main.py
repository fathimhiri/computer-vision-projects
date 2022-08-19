import cv2
import pickle
import cvzone
import numpy as np



cap = cv2.VideoCapture('carPark.mp4')
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)
width, height = 107, 48

def checkParkSpace(img):
    spacecounter = 0
    for pos in posList :
        x,y = pos
        imgcrop = img[y:y+height , x : x+width]
        count = cv2.countNonZero(imgcrop)
        
        if count < 900 :
            color = (0,255,0)
            thickness = 5
            spacecounter +=1
        else :
            color = (0,255,0)
            thickness = 2
        cv2.rectangle(frame,pos ,(x+width , y+height),color, thickness)
        cvzone.putTextRect(frame,f'Free : {spacecounter}/{len(posList)}',(100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))            

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    _,frame = cap.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3),1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    
    checkParkSpace(imgDilate)
    cv2.imshow("Image", frame)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgMedian)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
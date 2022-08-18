import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'imgs'
images = []
classN =[]

myList = os.listdir(path)
print(myList)

for i in myList:
    curImg = cv2.imread(f'{path}/{i}')
    images.append(curImg)
    classN.append(os.path.splitext(i)[0])
#print(images[0])
print(classN)


def findEncodings(images):
    encods=[]
    for i in images :
        i = cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(i)[0]
        encods.append(encode)
    return encods

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        now = datetime.now()
        dtString=now.strftime('%H:%M:%S')
        f.writelines(f'n{name},{dtString}')


encodeListKnown=findEncodings(images)
print('encoding finished')

cap = cv2.VideoCapture(0)

while True:
    _ , img = cap.read()

    FaceLoc = face_recognition.face_locations(img)
    print(FaceLoc) #face lcoations of the current frame
    encoding=face_recognition.face_encodings(img,FaceLoc)
    #cv2.rectangle(img ,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
    #print(encoding ,'/n/n/n/n')
    #print(faceLoc)
    
    for e , l in zip(encoding,FaceLoc)  :
        facesDis = face_recognition.face_distance(encodeListKnown, e)
        matches = face_recognition.compare_faces(encodeListKnown, e)
    #faceDis = face_recognition.face_distance(encodeListKnown, encoding)
        
    print(matches)
    print(facesDis)
    matchIndex = np.argmin(facesDis)
    #print(faceDis)  
    #if faceDis[matchIndex]< 0.50:
    if matches[matchIndex]:
        name = classN[matchIndex].upper()
    else: 
        name = 'Unknown'
    for f in FaceLoc:
        y1,x2,y2,x1 = f
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(img,(x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)
        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        markAttendance(name)
    
    cv2.imshow('Webcam',img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    



cap.release()
cv2.destroyAllWindows()    
        
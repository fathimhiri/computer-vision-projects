import cv2

import face_recognition


imgE=face_recognition.load_image_file('imgATT/elon.jpg')
imgE = cv2.cvtColor(imgE , cv2.COLOR_BGR2RGB)
imgB=face_recognition.load_image_file('imgATT/billT.jpg')
#imgB=face_recognition.load_image_file('imgATT/elonT.jpg')
imgB = cv2.cvtColor(imgB , cv2.COLOR_BGR2RGB)



faceLoc = face_recognition.face_locations(imgE) # a list
#print(faceLoc)
faceLoc = face_recognition.face_locations(imgE)[0]
encodeE=face_recognition.face_encodings(imgE)[0]
#print(encodeE)
cv2.rectangle(imgE ,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)  


faceLocB = face_recognition.face_locations(imgB)[0]
encodeB=face_recognition.face_encodings(imgB)[0]
cv2.rectangle(imgB ,(faceLocB[3],faceLocB[0]),(faceLocB[1],faceLocB[2]),(255,0,255),2)   

results = face_recognition.compare_faces([encodeE], encodeB)
faceDis = face_recognition.face_distance([encodeE], encodeB)

print(results)
print(faceDis)

cv2.imshow("elon",imgE)
cv2.imshow("bill",imgB)
k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
    








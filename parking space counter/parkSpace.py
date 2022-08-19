import cv2
import pickle

w  , h = 107,48

try :
    with open('carParkPos', 'rb') as f :
        posList = pickle.load(f)
except:
    posList = []       


def mouseClick(event,x,y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i , pos in enumerate(posList):
            if pos[0] <x< pos[0] + w  and pos[1]  <y< pos[1] +h :
                posList.pop(i)
    with open ('carParkPos','wb') as f :
        pickle.dump(posList,f)
    
    
while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + w, pos[1] + h), (255, 0, 255), 2)
 
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
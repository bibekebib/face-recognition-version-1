from cv2 import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
Id = input('enter your id: ')
sampleNum =0
while (1):
    _,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face.detectMultiScale(gray,1.5,5)
    for (x,y,w,h) in faces:
        img =cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),1)
        sampleNum = sampleNum +1
        cv2.imwrite('dataSet/user.'+Id+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.imshow('final', img)
    if cv2.waitKey(100) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break
    elif sampleNum >20:
        cap.release()
        cv2.destroyAllWindows()
        break




'''img = cv2.imread('crowd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)

cv2.imshow('final',img)
cv2.waitKey(0)'''
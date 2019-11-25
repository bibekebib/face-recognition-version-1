#all this are just importing the modules
from cv2 import cv2
import numpy as np 
import os
#here we are using LBPHFaceRecognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
#the dataset was prepared in last code and saved to this folder
recognizer.read('trainer/trainer.yml')
#the classifir algorithm used is haarcascade
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while (1):
    _, frame = cap.read() #reading each frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converting to gray for better operation of classifier
    faces = face.detectMultiScale(gray, 1.3,5)
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x-50, y-50),(x+w+50, y+h+50),(0,255,0),2)
      id, conf = recognizer.predict(gray[y:y+h, x:x+w])
      print(conf)
      if conf <70:
         if id==1:
            id = "Bibek Chalise"
            
         elif id == 2:
            id = "Bikram Chalise"
         
         elif id ==3:
            id ='Kishor chalise'
         
      else:
         id = " unknown"
      
        
      cv2.putText(frame, str(id), (x,y-35),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,250),1,cv2.LINE_AA)
    cv2.imshow("Face Recognizer",frame)
    if cv2.waitKey(10) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break

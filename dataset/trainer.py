from cv2 import cv2
import numpy as np 
import os
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def getimages(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    facesamples = []
    ids = []
    for imagepath in imagepaths:
        pilImage = Image.open(imagepath).convert('L')
        imageNp = np.array(pilImage,'uint8')
        Id = int(os.path.split(imagepath)[-1].split(".")[1])
        faces = detector.detectMultiScale(imageNp)
        for (x,y,w,h) in faces:
            facesamples.append(imageNp[y:y+h,x:x+w])
            ids.append(Id)
    return (facesamples,ids)

faces, ids = getimages('dataSet')
recognizer.train(faces,np.array(ids))
recognizer.write('trainer/trainer.yml')



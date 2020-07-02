# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:44:01 2020

@author: samsung
"""

import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("DSC00025.jpg")
gray_im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(gray_im,scaleFactor=1.05,minNeighbors=5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
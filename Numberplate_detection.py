# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:55:35 2020

@author: samsung
"""

import cv2

plate_cascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

img=cv2.imread("number_plate.png")
gray_im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


plates=plate_cascade.detectMultiScale(gray_im,scaleFactor=1.05,minNeighbors=5)
print(type(plates))
print(plates)

for x,y,w,h in plates:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
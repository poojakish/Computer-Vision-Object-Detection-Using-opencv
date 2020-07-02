

import cv2

body_cascade= cv2.CascadeClassifier("haarcascade_fullbody.xml")

cap=cv2.VideoCapture("pedestrians.mp4") # add your video here 

while True:
    ret,frame=cap.read()
    #detecting the pedestrians 
    body_rect=body_cascade.detectMultiScale(frame,1.3,5)
        
    for x,y,w,h in body_rect:
        frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,25,0),4)
            
    cv2.imshow('pedestians',frame)
    
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()

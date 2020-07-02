
import cv2

cars_cascade=cv2.CascadeClassifier("cars.xml")

cap=cv2.VideoCapture("video1.avi") # Add your vehicle video here.

while True:
    ret,frame=cap.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cars=cars_cascade.detectMultiScale(gray,1.3,5)
    
    for x,y,w,h in cars:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            
    cv2.imshow("Car Detection",frame)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

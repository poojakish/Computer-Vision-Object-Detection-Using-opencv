

import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cas=cv2.CascadeClassifier("haarcascade_eye.xml")
img=cv2.imread("POOJA.jpg")
gray_im=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces=face_cascade.detectMultiScale(gray_im,scaleFactor=1.05,minNeighbors=5)
eyes=eye_cas.detectMultiScale(gray_im,1.3,5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
for x,y,w,h in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

resized=cv2.resize(img,(int(img.shape[1]/7),int(img.shape[0]/7)))

cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

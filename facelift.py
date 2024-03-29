import cv2

face_cascade = cv2.CascadeClassifier('C:\Users\calda\Desktop\haarcascade_frontalface_default.xml')

img = cv2.imread('C:\Users\calda\Desktop\proasta.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMuktiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
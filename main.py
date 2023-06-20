import cv2

image = cv2.imread('C:\\Users\\harsh\\Python Scripting\\Face Detectors\\humans.jpeg',1)
face_cascade = cv2.CascadeClassifier('C:\\Users\\harsh\\Python Scripting\\Face Detectors\\faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),4)
cv2.imwrite('C:\\Users\\harsh\\Python Scripting\\Face Detectors\\humans.jpeg',image)
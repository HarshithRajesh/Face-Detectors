import cv2
import os

CASCADE = 'C:\\Users\\harsh\\Python Scripting\\Face Detectors\\faces.xml'
INPUT_FOLDER = 'C:\\Users\\harsh\\Python Scripting\\Face Detectors\\input'
OUTPUT_FOLDER = 'C:\\Users\\harsh\\Python Scripting\\Face Detectors\\output'
COLOUR = (255,255,255)
WIDTH = 4
SCALE = 1.1
NEIGHBOURS = 4

def has_face(image_path):
    image = cv2.imread(image_path,1)
    face_cascade = cv2.CascadeClassifier(CASCADE)
    faces = face_cascade.detectMultiScale(image,SCALE,WIDTH)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),4)
    return image

images = os.listdir(INPUT_FOLDER)
for image in images:
    face_image= has_face(f'{INPUT_FOLDER}\\{image}')
    if face_image is not None:
        cv2.imwrite(f'{OUTPUT_FOLDER}\\{image}',face_image)
import cv2
import math
face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fan_off_cascade = cv2.CascadeClassifier('fan_cascade.xml')


pic = cv2.imread('project_detect.jpg',0)
scale_factor = 1.3
faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
fan = fan_off_cascade.detectMultiScale(pic, scale_factor, 5)
face_a=0
face_b=0
fan_x=0
fan_y=0
#face
for (a,b,w,h) in faces:
    cv2.rectangle(pic, (a,b), (a+w, b+h), (255,0,0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(pic,'Face Detected',(a,b), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    face_a=a
    face_b=b
    
noOfFace = format(len(faces))
    
print("Number of faces found {}", noOfFace)
print("face a{}",face_a)
print("face b{}",face_b)

#fan
for (x,y,w,h) in fan:
    cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(pic,'Fan Detected',(x,y), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    fan_x=x
    fan_y=y
    
noOfFan = format(len(fan))
    
print("Number of fan found {}", noOfFan)
print("fan x{}",fan_x)
print("fan y{}",fan_y)

#Distance
distance = math.sqrt((face_b - face_a)*(face_b - face_a) + (fan_y - fan_x)*(fan_y - fan_x))
print("Distance {}",distance)
    
img = cv2.resize(pic, (960, 540))
cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
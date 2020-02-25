#import the library opencv
import cv2
#globbing utility.
import glob
#select the path
import math
import os

video=cv2.VideoCapture(0)
i=0
face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fan_off_cascade = cv2.CascadeClassifier('fan_cascade.xml')
#I have provided my path from my local computer, please change it accordingly
scale_factor = 1.3
face_a=0
face_b=0
fan_x=0
fan_y=0
path = "E:\Photo\propic\*.*"
while True:
    check, frame = video.read()
    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(1) 
    if key == ord ('x'):
        i+=1
        cv2.imwrite('image'+str(i)+'.jpg', frame)
        cv2.imshow("Captured", frame)
        print('taking pictures')
        for file in glob.glob(path):
            print(file)
            pic= cv2.imread(file)
            cv2.waitKey(1000)
            faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
            fan = fan_off_cascade.detectMultiScale(pic, scale_factor, 5)
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
            cv2.imshow('face', img)
    if key == ord ('q'):
        break
        cv2.waitKey(1)
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
        
#import the library opencv
import cv2
#globbing utility.
import glob
#select the path
face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#I have provided my path from my local computer, please change it accordingly
scale_factor = 1.3

path = "E:\Photo\propic\*.*"
for file in glob.glob(path):
    print(file)
    pic= cv2.imread(file)
    cv2.waitKey(1000)
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    print(faces)
#face
    for (a,b,w,h) in faces:
        cv2.rectangle(pic, (a,b), (a+w, b+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'Face Detected',(a,b), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    
    noOfFace = format(len(faces))
        
    print("Number of faces found {}", noOfFace)
    img = cv2.resize(pic, (960, 540))
    cv2.imshow('face', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
import cv2

face_cascade =cv2.CascadeClassifier('fan_cascade.xml')
fan_off_cascade = cv2.CascadeClassifier('fan_cascade.xml')
light_off_cascade = cv2.CascadeClassifier("cascade.xml")
videocapture = cv2.VideoCapture(0)
scale_factor = 1.3

while True:
    ret, pic = videocapture.read()
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)
    fan = fan_off_cascade.detectMultiScale(pic, scale_factor, 5)
    light = light_off_cascade.detectMultiScale(pic, scale_factor, 5)
    print(faces)
    print(fan)
    #face
    for (x,y,w,h) in faces:
        cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'Face Detected',(x,y), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
    noOfFace = format(len(faces))
        
    print("Number of faces found {}", noOfFace)
    #fan
    for (x,y,w,h) in fan:
        cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'Fan Detected',(x,y), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
    noOfFan = format(len(fan))
        
    print("Number of fan found {}", noOfFan)
    
    #light
    for (x,y,w,h) in light:
        cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(pic,'light Detected',(x,y), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        
    noOfLight = format(len(light))
        
    print("Number of light found {}", noOfLight)
    
    
    
        
        
    cv2.imshow('face', pic)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
videocapture.release()
cv2.destroyAllWindows()
        
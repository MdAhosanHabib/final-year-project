import cv2
import os
video=cv2.VideoCapture(0)
i=0
path = 'F:\Python\final project\Images'
while True:
    check, frame = video.read()
    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(1) 
    if key == ord ('x'):
        i+=1
        cv2.imwrite(('F:\Python\final project\Images\')'image'+str(i)+'.jpg'), frame)
        cv2.imshow("Captured", frame)
        print('taking pictures')
    if key == ord ('q'):
        break
        cv2.waitKey(1)
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows


import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread(r"C:\Users\hp\Pictures\mobile\IMG_20190721_132048.jpg")
img = cv2.resize(img,(512,512))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

img= gray[y-32:y+h+32,x-32:x+w+32]
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
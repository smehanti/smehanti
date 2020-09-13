import cv2

imagepath='/Users/saurabhmehanti/Desktop/IMG_2545.jpg'
cascpath='/Users/saurabhmehanti/Desktop/haarcascade_frontalface_default.xml'
image=cv2.imread(imagepath)

face=cv2.CascadeClassifier(cascpath)

myface=face.detectMultiScale(image,minSize=(55,55),scaleFactor=2.1,minNeighbors=9,flags=cv2.CASCADE_SCALE_IMAGE)

# print(myface)

for (x,y,w,h) in myface:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Faces found',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


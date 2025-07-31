import cv2
faces=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("kat.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=faces.detectMultiScale(gray,1.1,2)
for x,y,w,h in f:
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,56,38),3)
cv2.imshow("Face detection ",img)
while True:
    key=cv2.waitKey()
    if key==27 or key==ord('q'):
        break
cv2.destroyAllWindows()
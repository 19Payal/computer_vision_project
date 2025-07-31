import cv2
eyes=cv2.CascadeClassifier("haarcascade_eye.xml")
img=cv2.imread("kat.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
e=eyes.detectMultiScale(gray,1.1,2)
for x,y,w,h in e:
    cv2.rectangle(img,(x,y),(x+w,y+h),(201,50,39),3)
cv2.imshow("Eyes detection: ",img)

while True:
    key=cv2.waitKey(0)
    if key==27 or key==ord('q'):
        break
cv2.destroyAllWindows()


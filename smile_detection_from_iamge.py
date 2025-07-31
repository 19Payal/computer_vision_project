import cv2
smile=cv2.CascadeClassifier("haarcascade_smile.xml")
img=cv2.imread("kat.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
s=smile.detectMultiScale(gray,1.1,3)
for x,y,w,h in s:
    cv2.rectangle(img,(x,y),(x+w,y+h),(488,46,38),2)
cv2.imshow("Smile detection ",img)
key=cv2.waitKey()
while True:
   if key==27 or key==ord('q'):
       break
cv2.destroyAllWindows()
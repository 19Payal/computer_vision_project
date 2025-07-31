import cv2
img=cv2.imread('capture.JPG')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
edges=cv2.Canny(blur,50,200)
contours ,hierarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),5)
cv2.imshow("Contours detection ",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

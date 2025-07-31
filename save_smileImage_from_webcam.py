import cv2
video=cv2.VideoCapture(0)
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smilecascade=cv2.CascadeClassifier("haarcascade_smile.xml")
cnt=500
while True:
    success,img=video.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(grayimg,1.1,4)
   
    keypress=cv2.waitKey(1)
    for (x,y,w,h)in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),5)
        smiles=smilecascade.detectMultiScale(grayimg,1.8,15)
        for (x,y,w,h) in smiles:
            img=cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),5)
            print("image"+str(cnt),"Saved")
            path="smile_Image"+str(cnt)+".jpg"
            cv2.imwrite(path,img)
            cnt+=1
        if(cnt<=503):
          break
    cv2.imshow("smile detection",img)
    if(keypress & 0xff ==ord('q')):
        break
video.release()
cv2.destroyAllWindows()
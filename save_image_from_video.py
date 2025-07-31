import cv2 
save_img=100
cap=cv2.VideoCapture(r"4K Road traffic video.mp4")
sec=0.0
framerate=1
while True:
    try:
        _,img=cap.read()
        print("Cpaturing")
        sec+=framerate
        n = int(input("Enter count"))
        for x in range(n):
          save_img+=1
          cv2.imwrite(f".\capture_Image\cap_{save_img}.jpg".format(),img)
    except Exception as e:
        print("there is exp: {}",format(e))
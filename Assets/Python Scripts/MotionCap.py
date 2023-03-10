import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("dance_video.mp4")

detector = PoseDetector()
posList = []

while True:
    success,img = cap.read()
    detector.findPose(img)
    lmList,bBoxInfo = detector.findPosition(img)

    if bBoxInfo:
        lmString = ""
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'

        posList.append(lmString)    

    print(len(posList))

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)

    if key == ord("s"):
        with open("AnimationFile.txt",'w') as f:
            f.writelines(["%s\n" % item for item in posList])
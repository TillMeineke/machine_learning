import time
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)

pTime = 0
while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
            (255, 0, 0), 3)
    cv2.imshow('Image', img)

    cv2.waitKey(1)

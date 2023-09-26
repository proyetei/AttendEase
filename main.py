import cv2
import os

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# add a path and then for loop for importing the images for the 4 different modes into a list
# MODES: active, marked, already marked, scanning the student
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in folderModePath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath))) 

# run the webcam
while True:
    success, img=cap.read()
    
    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[2]
    

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
    

print("hello world")
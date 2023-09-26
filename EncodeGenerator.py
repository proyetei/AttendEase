import cv2
import face_recognition
import pickle
import os

#importing the student images
folderPath = 'Images'
pathList = os.listdir(folderPath)

imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0]) #extracts the studentIDs

#loops through the images and encodes them
def findEncodings(imagesList):
    encodeList = []

    for img in imagesList:
        #change the colour space
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #gets the encodings
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodingListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", "wb")
pickle.dump(encodingListKnownWithIds, file) #dump the image encodings along with the studentIds into the file
file.close()
print("File saved")
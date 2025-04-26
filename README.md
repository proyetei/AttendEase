# AttendEase
## About The Project

AttendEase is a student attendance tracking software that leverages facial recognition technology. It utilizes a webcam to capture images, employs the Haar Cascade algorithm for face detection, and integrates with Google Cloud Platform (GCP) and Firebase for data management. The system identifies students and automatically records their attendance, streamlining the attendance process.


## Pre-requisites:
-Pipenv (latest version)

## How to use:
In the initial run, run EncodeGenerator.py and AddDatatoDatabse.py to generate image encoding and store the initial data in database
After that, run main.py to use the attendance system.


### Key Features

- **Facial Recognition:** Uses OpenCV and the Haar Cascade algorithm for accurate face detection.
- **Real-time Attendance Tracking:** Automatically marks attendance when a student's face is recognized.
- **Firebase Integration:** Stores and manages student data, including attendance records, using Firebase Realtime Database and Storage.
- **Webcam Integration:** Captures video feed from a webcam for facial recognition.
- **Encoding Generation:** Generates and stores face encodings for efficient recognition.
- **Attendance Reporting:** Provides data on student attendance, including total attendance and last attendance time.


The project is built using Python and relies on several key libraries:

- **OpenCV (cv2):**  Used for image processing and face detection.
- **face_recognition:** Provides face encoding and comparison functionalities.
- **cvzone:** Simplifies common OpenCV tasks, such as drawing bounding boxes.
- **Firebase Admin SDK:** Enables interaction with Firebase services, including Realtime Database and Storage.
- **pickle:** Used for serializing and deserializing face encodings.

The system operates as follows:

1.  **Image Capture:** The webcam captures real-time video frames.
2.  **Face Detection:** OpenCV's Haar Cascade algorithm identifies faces within the frames.
3.  **Encoding Generation/Loading:** Face encodings are either generated from student images (using `EncodeGenerator.py`) and stored in `EncodeFile.p`, or loaded from the existing file.
4.  **Facial Recognition:** The `face_recognition` library compares the detected face encodings with the known encodings stored in `EncodeFile.p`.
5.  **Attendance Marking:** Upon successful recognition, the system updates the student's attendance record in the Firebase Realtime Database.
6.  **Data Storage:** Student images are stored in Firebase Storage, and student data (name, major, attendance, etc.) is stored in the Firebase Realtime Database.
7.  **User Interface:**  The `main.py` script displays a user interface with real-time video feed and student information.


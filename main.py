import handle_directories_and_files as manageDir
import face_detection as faceDetection
import motion_detector as detector

path = "images"

def getUserInput():
    userAnswer = input("Do you want to show video frame? (Y/N) : ").lower()
    while not(userAnswer == "y" or userAnswer == "yes" or userAnswer == "n" or userAnswer == "no"):
        print("Input yes (y) or no (n)")
        userAnswer = input("Do you want to show video frame? (Y/N) : ").lower()
    if userAnswer == "y":
        return True
    else:
        return False

# Create required directory
manageDir.CreateDirectory(path)

# Capture object in image if objects are different
faceDetection.captureImageOnFaceDetection(path, getUserInput())

# capture the object time when object is detected in webcam
# detector.ObjectDetector()
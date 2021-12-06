import cv2
from datetime import datetime
haar_file = 'haarcascade\\haarcascade_frontalface_default.xml'

def captureImageOnFaceDetection(path, isVideoFramVisible):
    (width, height) = (1280, 720)  # defining the size of images
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)

    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
            face = gray
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('%s/%s' % (path, datetime.now().strftime("%d%m%Y%H%M%S")+".png"), face_resize)

        # show webcam frame
        if isVideoFramVisible == True:
            cv2.imshow('OpenCV', im)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()
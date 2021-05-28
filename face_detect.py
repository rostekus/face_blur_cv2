import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:


    is_successful_frame , frame = webcam.read()

    if is_successful_frame:
        gray_scaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('hello', gray_scaled_img)
        cv2.waitKey(1)




img = cv2.imread('apl.jpeg')
print("hello")
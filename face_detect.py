import cv2

DRAW_RECTANGLE = False
RGB_COLOR_FRAME = (0, 255, 0)  # Green

trained_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:

    is_successful_frame, frame = webcam.read()
    result_image = frame.copy()

    if is_successful_frame:
        grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        faces = trained_face_data.detectMultiScale(grayimg,
                                                   scaleFactor=1.1,
                                                   minNeighbors=6)

        if len(faces) != 0:  # If there are faces in the images
            for f in faces:  # For each face in the image

                # Get the origin co-ordinates and the length and width till where the face extends
                x, y, w, h = [v for v in f]

                # Get the rectangle img around all the faces
                if DRAW_RECTANGLE:
                    cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  RGB_COLOR_FRAME, 2)

                sub_face = frame[y:y + h, x:x + w]
                height, width = sub_face.shape[:2]
                w, h = (16, 16)
                temp = cv2.resize(sub_face, (w, h),
                                  interpolation=cv2.INTER_LINEAR)
                sub_face = cv2.resize(temp, (width, height),
                                      interpolation=cv2.INTER_NEAREST)
                # Merge face image our final image
                result_image[y:y + sub_face.shape[0],
                             x:x + sub_face.shape[1]] = sub_face

    key = cv2.waitKey(1)
    cv2.imshow('hello', result_image)

    if key == ord('q'):
        break
webcam.release()

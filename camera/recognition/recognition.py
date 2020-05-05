import face_recognition
import cv2
import numpy as np


class FaceManagement:
    known_face_image_file = None
    known_face_image_encoding = None
    know_face_name = None


class FaceRecognition:
    camera_index = None
    faces = list()

    def __init__(self, camera_index):
        if camera_index is not None:
            self.camera_index = camera_index
        if self.camera_index is None:
            raise Exception('Camera index must be passed')
        self.video_capture = cv2.VideoCapture(self.camera_index)

    def recognize(self, camera_index):
        video_capture = cv2.VideoCapture(camera_index)

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        # try:
        while True:

            # grab a single frame of video
            ret, frame = video_capture.read()
            if frame is None:
                print('frame is None')
                continue
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            print(small_frame)

            # convert the image from BGR color (which OpenCV uses) to RGB
            rgb_frame = small_frame[:, :, ::-1]

            # find all the faces and face encodings in the frame of video
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Loop through each face in this frame of video
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, 'noi', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # display the resulting image
            cv2.imshow('Video', frame)


        # except Exception as e:
        #     print(e.__str__())
        # finally:
        self.video_capture.release()
        cv2.destroyAllWindows()

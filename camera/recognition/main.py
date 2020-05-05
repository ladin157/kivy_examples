import kivy_threading

import cv2
from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from camera.recognition.recognition import FaceRecognition

Builder.load_file('recog.kv')


def is_device(source):
    cap = cv2.VideoCapture(source)
    if cap is None or not cap.isOpened():
        return False
    else:
        return True


class Recognition(BoxLayout):
    camera_id = ObjectProperty()
    camera_index = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.camera_index)
        print(self.camera_id)

    def recognize(self):
        if is_device(0):
            self.camera_index = 0
        elif is_device(1):
            self.camera_index = 1
        recogntion = FaceRecognition(camera_index=self.camera_index)
        recog_thread = kivy_threading.Thread(target=recogntion.recognize, args=(self.camera_index,))
        recog_thread.daemon = True
        recog_thread.start()


class RecognitionApp(App):
    def build(self):
        return Recognition()


RecognitionApp().run()

from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from camera.recognition.recognition import FaceRecognition

Builder.load_file('recog.kv')


class Recognition(BoxLayout):
    camera_id = ObjectProperty()
    camera_index = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.camera_index)
        print(self.camera_id)

    def recognize(self):
        recogntion = FaceRecognition(camera_index=self.camera_index)
        recogntion.recognize()


class RecognitionApp(App):
    def build(self):
        return Recognition()


RecognitionApp().run()

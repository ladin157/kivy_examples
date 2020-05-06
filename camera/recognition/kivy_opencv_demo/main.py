# coding=utf-8
# qpy:kivy

import time

import cv2
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.core.camera import Camera
from kivy.core.image import Texture
from kivy.uix.boxlayout import BoxLayout


class Camera2(Camera):
    firstFrame = None

    def _camera_loaded(self, *largs):
        if kivy.platform == 'android':
            self.texture = Texture.create(size=self.resolution, colorfmt='rgb')
            self.texture_size = list(self.texture.size)
        else:
            super(Camera2, self)._camera_loaded()

    def on_tex(self, *l):
        if kivy.platform == 'android':
            buf = self._camera.grab_frame()
            if not buf:
                return
            frame = self._camera.decode_frame(buf)
            self.image = frame = self.process_frame(frame)
            buf = frame.tostring()
            self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        super(Camera2, self).on_tex(*l)

    def process_frame(self, frame):
        r, g, b = cv2.split(frame)
        frame = cv2.merge((b, g, r))
        rows, cols, channel = frame.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
        dst = cv2.warpAffine(frame, M, (cols, rows))
        frame = cv2.flip(dst, 1)
        if self.index == 1:
            frame = cv2.flip(dst, -1)
        return frame


class MyLayout(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return MyLayout()

    def on_start(self):
        Clock.schedule_once(self.detect, 5)

    def detect(self, nap):
        image = self.root.ids.camera.image
        rows, cols = image.shape[:2]
        ctime = time.ctime()[11:19]
        self.root.ids.label.text = '%s image rows:%d cols:%d' % (ctime, rows, cols)
        Clock.schedule_once(self.detect, 1)


if __name__ == '__main__':
    MainApp().run()

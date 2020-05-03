from random import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle, Line, Triangle


class PaintWidget(TextInput):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            # Ellipse(pos=(touch.x - d / 2.0, touch.y - d / 2.0), size=(d, d))
            # Rectangle(pos=(touch.x - d / 2.0, touch.y - d / 2.0), size=(d, d))
            x, y = touch.x, touch.y
            print(x, y)
            Triangle(points=[x - d / 2, y + d / 2, x + d / 2, y + d / 2, x, y - d / 2])
            print(self.x, self.y, self.size)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.paint = PaintWidget()
        self.add_widget(self.paint)
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        self.add_widget(clearbtn)

    def clear_canvas(self, obj):
        self.paint.canvas.clear()

class PaintScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = PainLayout()
        self.add_widget(layout)


class PaintApp(App):
    def build(self):
        return PaintScreen()


if __name__ == '__main__':
    PaintApp().run()

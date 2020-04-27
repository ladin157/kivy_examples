from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = '900'

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text='Hello world',
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
        )
        return screen


MainApp().run()

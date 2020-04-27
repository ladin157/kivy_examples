from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'

        screen = Screen()
        md_button = MDRectangleFlatButton()
        md_button.text = 'Hello world'
        md_button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        screen.add_widget(md_button)

        return screen


MainApp().run()

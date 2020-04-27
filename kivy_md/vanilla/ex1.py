from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        mdlabel = MDLabel()
        mdlabel.text = 'Hello, World'
        mdlabel.halign = 'center'
        mdlabel.size_hint = 0.1, 0.5
        return mdlabel


MainApp().run()

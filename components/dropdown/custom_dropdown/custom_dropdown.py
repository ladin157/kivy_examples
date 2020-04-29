from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class CustomDropDown(DropDown):
    pass


class DemoApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dropdown = CustomDropDown()
        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

    def build(self):
        pass


DemoApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder


Builder.load_string('''
<MyWidget>
    orientation: 'vertical'
    Spinner:
        id: auxlo
        text: "Select"
        values: ('On', 'Off')
        focus: True
        on_text: auxlonum.disabled = True if auxlo.text == 'Off' else False

    Label:

    Spinner:
        id: auxlonum
        text: "Select"
        values: ('# 1', '# 2')
        focus: True

    Label:
''')


class MyWidget(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        return  MyWidget()

TestApp().run()
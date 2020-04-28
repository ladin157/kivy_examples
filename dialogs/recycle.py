from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

KV = '''
<CusLabel@Label>:
    font_size: 14

<RecycleItem>:
    orientation: 'horizontal'
    BoxLayout:
        size_hint_x: 0.3
        Image:
            size_hint: 0.8, 0.8
            source: ''
    BoxLayout:
        size_hint_x: 0.7
        orientation: 'vertical'
        BoxLayout: # first row
            size_hint_y: 0.3
            Label:
                size_hint_x: 0.6
                text: '2020/03/03'
            CusLabel:
                size_hint_x: 0.4
                text: '12:34'

        BoxLayout: # second row
            size_hint_y: 0.4
            CusLabel:
                halign: 'center'
                text: 'Registered Name'

        BoxLayout: # third row
            size_hint_y: 0.3
            CusLabel:
                halign: 'right'
                text: 'Camera A'
'''

Builder.load_string(KV)


class RecycleItem(BoxLayout):
    pass


class TestBoxlayout(App):
    def build(self):
        return RecycleItem()


TestBoxlayout().run()

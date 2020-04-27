from kivy.lang import Builder

from kivy.app import App
from kivy.uix.button import Button
from dialogs.dialog import Dialog

KV = '''
FloatLayout:

    Button:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''


class Example(App):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = Dialog(
                text="Discard draft?",
                buttons=[
                    Button(
                        text="CANCEL"
                    ),
                    Button(
                        text="DISCARD"
                    ),
                ],
            )
        self.dialog.open()

Example().run()
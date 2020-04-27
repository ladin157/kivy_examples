from kivy.clock import Clock
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

KV = '''
<ContentInputDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    Label:
        font_style: 'H6'
        text: root.title
        halign: 'left' if not root.device_ios else 'center'

    BoxLayout:
        id: box_input
        size_hint: 1, None

    Widget:
    Widget:

    Separator:
        id: sep

    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0


<ContentDialog>
    orientation: 'vertical'
    padding: dp(15)
    spacing: dp(10)

    text_button_ok: ''
    text_button_cancel: ''

    Label:
        id: title
        text: root.title
        font_style: 'H6'
        halign: 'left' if not root.device_ios else 'center'
        valign: 'top'
        size_hint_y: None
        text_size: self.width, None
        height: self.texture_size[1]

    ScrollView:
        id: scroll
        size_hint_y: None
        height:
            root.height - (box_buttons.height + title.height + dp(48)\
            + sep.height)

        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                #source: f'{images_path}dialog_in_fade.png'
                source: f'{images_path}transparent.png'

        Label:
            text: '\\n' + root.text + '\\n'
            size_hint_y: None
            height: self.texture_size[1]
            valign: 'top'
            halign: 'left' if not root.device_ios else 'center'
            markup: True

    Separator:
        id: sep

    BoxLayout:
        id: box_buttons
        size_hint_y: None
        height: dp(20)
        padding: dp(20), 0, dp(20), 0
'''

Builder.load_string(KV)


class BaseDialog(FloatLayout):
    def set_content(self, instance_content_dialog):
        def _events_callback(result_press):
            self.dismiss()
            if result_press and self.events_callback:
                self.events_callback(result_press, self)

        if self.device_ios:  # create buttons for iOS
            self.background = self._background

            if instance_content_dialog.__class__ is ContentInputDialog:
                self.text_field = TextInput(
                    pos_hint={"center_x": 0.5},
                    size_hint=(1, None),
                    multiline=False,
                    height=dp(33),
                    cursor_color=self.theme_cls.primary_color,
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(33)
                instance_content_dialog.ids.box_input.add_widget(
                    self.text_field
                )

            if self.text_button_cancel != "":
                anchor = "left"
            else:
                anchor = "center"
            box_button_ok = AnchorLayout(anchor_x=anchor)
            box_button_ok.add_widget(
                Button(
                    text=self.text_button_ok,
                    font_size="18sp",
                    on_release=lambda x: _events_callback(self.text_button_ok),
                )
            )
            instance_content_dialog.ids.box_buttons.add_widget(box_button_ok)

            if self.text_button_cancel != "":
                box_button_ok.anchor_x = "left"
                box_button_cancel = AnchorLayout(anchor_x="right")
                box_button_cancel.add_widget(
                    Button(
                        text=self.text_button_cancel,
                        font_size="18sp",
                        on_release=lambda x: _events_callback(
                            self.text_button_cancel
                        ),
                    )
                )
                instance_content_dialog.ids.box_buttons.add_widget(
                    box_button_cancel
                )

        else:  # create buttons for Android
            if instance_content_dialog.__class__ is ContentInputDialog:
                self.text_field = TextInput(
                    size_hint=(1, None),
                    height=dp(48),
                    hint_text=instance_content_dialog.hint_text,
                )
                instance_content_dialog.ids.box_input.height = dp(48)
                instance_content_dialog.ids.box_input.add_widget(
                    self.text_field
                )
                instance_content_dialog.ids.box_buttons.remove_widget(
                    instance_content_dialog.ids.sep
                )

            box_buttons = AnchorLayout(
                anchor_x="right", size_hint_y=None, height=dp(30)
            )
            box = BoxLayout(size_hint_x=None, spacing=dp(5))
            box.bind(minimum_width=box.setter("width"))
            button_ok = Button(
                text=self.text_button_ok,
                on_release=lambda x: _events_callback(self.text_button_ok),
            )
            box.add_widget(button_ok)

            if self.text_button_cancel != "":
                button_cancel = Button(
                    text=self.text_button_cancel,
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: _events_callback(
                        self.text_button_cancel
                    ),
                )
                box.add_widget(button_cancel)

            box_buttons.add_widget(box)
            instance_content_dialog.ids.box_buttons.add_widget(box_buttons)
            instance_content_dialog.ids.box_buttons.height = button_ok.height
            instance_content_dialog.remove_widget(
                instance_content_dialog.ids.sep
            )


class ContentInputDialog(BoxLayout):
    title = StringProperty()
    hint_text = StringProperty()
    text_button_ok = StringProperty()
    text_button_cancel = StringProperty()
    device_ios = BooleanProperty()


class ContentDialog(BoxLayout):
    title = StringProperty()
    text = StringProperty()
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty()
    device_ios = BooleanProperty()


class InputDialog(BaseDialog):
    title = StringProperty("Title")
    hint_text = StringProperty()
    text_button_ok = StringProperty("Ok")
    text_button_cancel = StringProperty()
    events_callback = ObjectProperty()

    # _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.content_dialog = ContentInputDialog(
            title=self.title,
            hint_text=self.hint_text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(self.content_dialog)
        self.set_content(self.content_dialog)
        Clock.schedule_once(self.set_field_focus, 0.5)

    def set_field_focus(self, interval):
        self.text_field.focus = True


class Dialog(BaseDialog):
    title = StringProperty("Title")
    text = StringProperty("Text dialog")
    text_button_cancel = StringProperty()
    text_button_ok = StringProperty("Ok")
    events_callback = ObjectProperty()

    # _background = StringProperty(f"{images_path}ios_bg_mod.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        content_dialog = ContentDialog(
            title=self.title,
            text=self.text,
            text_button_ok=self.text_button_ok,
            text_button_cancel=self.text_button_cancel,
            device_ios=self.device_ios,
        )
        self.add_widget(content_dialog)
        self.set_content(content_dialog)

# class LoadDialog(FloatLayout):
#     load = ObjectProperty(None)
#     cancel = ObjectProperty(None)
#
#
# class SaveDialog(FloatLayout):
#     save = ObjectProperty(None)
#     text_input = ObjectProperty(None)
#     cancel = ObjectProperty(None)
#
#

from kivy import Logger
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class ComboBox(TextInput):
    options = ListProperty(('',))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ddn = self.drop_down = DropDown()
        ddn.bind(on_select=self.on_select)
        # super(ComboBox, self).__init__(**kw)

    def on_options(self, instance, value):
        ddn = self.drop_down
        ddn.clear_widgets()
        for widg in value:
            widg.bind(on_release=lambda btn: ddn.select(btn.text))
            ddn.add_widget(widg)

    def on_select(self, *args):
        self.text = args[1]

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            self.drop_down.open(self)
        return super(ComboBox, self).on_touch_up(touch)


class CustomDropDown(DropDown):
    pass


class ComboEdit(TextInput):
    options = ListProperty(('',))

    def __init__(self, **kw):
        ddn = self.drop_down = DropDown()
        ddn.bind(on_select=self.on_select)
        super(ComboEdit, self).__init__(**kw)

    def on_options(self, instance, value):
        ddn = self.drop_down
        ddn.clear_widgets()
        for widg in value:
            widg.bind(on_release=lambda btn: ddn.select(btn.text))
            ddn.add_widget(widg)

    def on_select(self, *args):
        self.text = args[1]

    def on_touch_up(self, touch):
        if touch.grab_current == self:
            self.drop_down.open(self)
        return super(ComboEdit, self).on_touch_up(touch)


class SettingScreen(Screen):

    # Callback for the checkbox
    def __init__(self, **kwargs):
        super(SettingScreen, self).__init__(**kwargs)
        for id in self.ids:
            print(id)
        # self.init_dropdowns()

    # def init_dropdowns(self):
    #     dropdown = CustomDropDown()
    #     mainbutton = Button(text='Hello', size_hint=(0.15, 0.05), pos_hint={'x': 0.26, 'top': 0.88})
    #     mainbutton.bind(on_release=dropdown.open)
    #     dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    #     self.add_widget(mainbutton)

    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

    def save(self):
        cam1_enable = self.ids['checkbox_1'].active
        cam1_type = self.ids['txtinput_observ_1'].text
        cam1_camera = self.ids['txtinput_camera_1'].text
        cam1_ip = self.ids['txtinput_ip_1'].text
        cam1_time = self.ids['txtinput_observ_time_1'].text

        cam2_enable = self.ids['checkbox_2'].active
        cam2_type = self.ids['txtinput_observ_2'].text
        cam2_camera = self.ids['txtinput_camera_2'].text
        cam2_ip = self.ids['txtinput_ip_2'].text
        cam2_time = self.ids['txtinput_observ_time_2'].text

        folder_enable = self.ids['checkbox_3'].active
        folder_path = self.ids['txtinput_observ_folder'].text
        folder_time = self.ids['txtinput_observ_time_3'].text

        # setting up
        smtp_server = self.ids['txtinput_smtp'].text
        mail_address = self.ids['txtinput_mail'].text
        # username = self.ids['txtinput_username'].text
        password = self.ids['txtinput_password'].text

        cam1 = dict()
        cam1_add = False
        # if cam1_enable is not None:
        #     cam1['cam1_enable'] = cam1_enable
        #     cam1_add = True
        if cam1_type is not None and not str(cam1_type).strip().__eq__(''):
            cam1['cam1_type'] = cam1_type
            cam1_add = True
        if cam1_camera is not None and not str(cam1_camera).strip().__eq__(''):
            cam1['cam1_camera'] = cam1_camera
            cam1_add = True
        if cam1_ip is not None and not str(cam1_ip).strip().__eq__(''):
            cam1['cam1_ip'] = cam1_ip
            cam1_add = True
        if cam1_time is not None and not str(cam1_time).strip().__eq__(''):
            cam1['cam1_time'] = cam1_time
            cam1_add = True

        cam2 = dict()
        cam2_add = False
        # if cam2_enable is not None:
        #     cam2['cam2_enable'] = cam2_enable
        #     cam2_add = True
        if cam2_type is not None and not str(cam2_type).strip().__eq__(''):
            cam2['cam2_type'] = cam2_type
            cam2_add = True
        if cam2_camera is not None and not str(cam2_camera).strip().__eq__(''):
            cam2['cam2_camera'] = cam2_camera
            cam2_add = True
        if cam2_ip is not None and not str(cam2_ip).strip().__eq__(''):
            cam2['cam2_ip'] = cam2_ip
            cam2_add = True
        if cam2_time is not None and not str(cam2_time).strip().__eq__(''):
            cam2['cam2_time'] = cam2_time
            cam2_add = True

        items = dict()
        if cam1_add and cam1_enable:
            items['cam1'] = cam1.__str__()
        if cam2_add and cam2_enable:
            items['cam2'] = cam2.__str__()

        folder = dict()
        folder_add = False
        if folder_path is not None and not str(folder_path).strip().__eq__(''):
            folder['folder_path'] = folder_path
            folder_add = True
        if folder_time is not None and not str(folder_time).strip().__eq__(''):
            folder['folder_time'] = folder_time
            folder_add = True
        if folder_add:
            items['folder'] = folder

        if smtp_server is not None and not str(smtp_server).strip().__eq__(''):
            items['smtp_server'] = smtp_server
        if mail_address is not None and not str(mail_address).strip().__eq__(''):
            items['mail_address'] = mail_address
        if password is not None and not str(password).strip().__eq__(''):
            items['password'] = password

        setting = SettingOperation()
        result, message = setting.add(Object=None, items=items)
        if result:
            Logger.infor(message)
        else:
            Logger.error(message)

    def browse(self):
        pass

    def show_dropdown_object1_type(button, *largs):
        dp = DropDown()
        dp.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        for i in range(10):
            item = Button(text='hello %d' % i, size_hint_y=None, height=44)
            item.bind(on_release=lambda btn: dp.select(btn.text))
            dp.add_widget(item)
        dp.open(button)

    def touch_move_object1_type(instance, touch):
        instance.center = touch.pos

    def show_dropdown_object1_cam(button, *largs):
        dp = DropDown()
        dp.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        for i in range(10):
            item = Button(text='hello %d' % i, size_hint_y=None, height=44)
            item.bind(on_release=lambda btn: dp.select(btn.text))
            dp.add_widget(item)
        dp.open(button)

    def touch_move_object1_cam(instance, touch):
        instance.center = touch.pos

    def show_dropdown_object2_type(button, *largs):
        dp = DropDown()
        dp.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        for i in range(10):
            item = Button(text='hello %d' % i, size_hint_y=None, height=44)
            item.bind(on_release=lambda btn: dp.select(btn.text))
            dp.add_widget(item)
        dp.open(button)

    def touch_move_object2_cam(instance, touch):
        instance.center = touch.pos


# Builder.load_file(r'View/kv_file/setting_screen.kv')

with open('setting_screen.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class DemoApp(App):
    def build(self):
        return SettingScreen()


DemoApp().run()

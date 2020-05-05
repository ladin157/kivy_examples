import datetime
import kivy_threading
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.properties import NumericProperty, ListProperty, StringProperty, AliasProperty, ObjectProperty, \
    BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView


class RecycleItem(BoxLayout):
    created_date = StringProperty()
    created_time = StringProperty()
    username = StringProperty()
    camera = StringProperty()


class RealtimeScreen(Screen):
    cameraId = NumericProperty()

    data = ListProperty()
    view = ObjectProperty()
    log_text = StringProperty()

    def _get_data_for_widgets(self):
        return [
            {
                'created_date': item['created_date'],
                'created_time': item['created_time'],
                'username': item['username'],
                'camera': item['camera']
            }
            for _, item in enumerate(self.data)
        ]

    data_for_widgets = AliasProperty(_get_data_for_widgets, bind=['data'])

    def __init__(self, **kwargs):
        super(RealtimeScreen, self).__init__(**kwargs)
        self.cameraId = 0
        self.log_text = "Info: Detect new person"
        # self.scroll = self.ids['scroll'] #ScrollView()
        self.init_data()
        # self.init_console()
        # Clock.schedule_once(self.create_scrollview)

    def create_scrollview(self, dt):
        base = ["element {}".format(i) for i in range(40)]
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter("height"))
        self.init_scroll(layout=layout)
        # for element in base:
        #     layout.add_widget(Button(text=element, size=(50, 50), size_hint=(1, None),
        #                              background_color=(0.5, 0.5, 0.5, 1), color=(1, 1, 1, 1)))
        scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scrollview.add_widget(layout)
        self.view.add_widget(scrollview)

    def init_data(self):
        for i in range(5):
            item = dict()
            item['created_date'] = '2020/04/' + str(i + 1)
            item['created_time'] = '11:' + str(i + 10)
            item['username'] = 'user_' + str(i + 1)
            item['camera'] = 'camera 1'
            self.data.append(item)

    def text_markup(self, text, war_type='info'):
        # color = [0, 255, 0, 0]
        markup = '[color=00FF00]Info[/color][color=3333ff][/color]'
        if war_type.__eq__('info'):
            # color = [0, 255, 0, 0]
            markup = ' &bl;[color=00FF00]INFO[/color]&br; '
        if war_type.__eq__('error'):
            # color = [255, 0, 0, 0]
            markup = ' &bl;[color=FF0000]ERROR[/color]&br; '
        if war_type.__eq__('warning'):
            # color = [255, 255, 255, 0]
            markup = ' &bl;[color=FFFF00]WARNING[/color]&br; '
        text = markup + text
        # label = Label(text=text, color=color, size_hint=(None, None), size=(50, 50))
        # label.markup = True
        # return label
        return text

    def init_console(self):
        # self.ids['console_log'].add_widget(self.scroll)
        # self.init_scroll()
        # for id in self.ids:
        #     print(id)
        pass

    def init_scroll(self, layout):
        label_info = self.text_markup(text='Info: Information', war_type='info')
        label_error = self.text_markup(text='Error: ', war_type='error')
        label_warning = self.text_markup(text='Warning', war_type='warning')
        layout.add_widget(label_info)
        layout.add_widget(label_error)
        layout.add_widget(label_warning)

    # def capture(self):
    #     camera = self.ids['camera']
    #     timestr = time.strftime("%Y%m%d_%H%M%S")
    #     camera.export_to_png("images/Capture/IMG_{}.png".format(timestr))
    #     Logger.info('Application: Capture a image from camera.')
    #     Logger.info('Application: Create and start thread for face recognition.')
    #     face_rec_t = kivy_threading.Thread(target=face_recognition.facerec_from_webcam, args=(1,))
    #     face_rec_t.daemon = True  # kill thread on app close
    #     face_rec_t.start()
    #
    # def switchcamera(self):
    #     if self.cameraId == 0:
    #         self.cameraId = 1
    #     else:
    #         self.cameraId = 0
    #     Logger.info('Application: Switch camera to #%s', str(self.cameraId))
    #     stmp_connection.send_email(0)

    def play_stop_camera(self):
        # self.log_text += '\nCamera 1 is playing'
        camera = self.ids['camera']
        if camera.play:
            text = self.text_markup(text='Camera 1 is playing.', war_type='info')
            self.log_text += '\n' + datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + text  # ' INFOR: Camera 1 is playing.'
        else:
            text = self.text_markup(text='Camera 1 is stopped.', war_type='warning')
            self.log_text += '\n' + datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + text  # ' INFOR: Camera 1 is stopped.'
        # print(self.log_text)


with open('realtime_screen.kv', encoding='utf8') as f:
    Builder.load_string(f.read())


class DemoApp(App):
    def build(self):
        return RealtimeScreen()


DemoApp().run()

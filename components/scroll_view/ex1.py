import kivy
from kivy.uix.label import Label

kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


class ScrollViewApp(App):

    def build(self):

        # create a default grid layout with custom width/height
        layout = GridLayout(cols=1, padding=10, spacing=10,
                size_hint=(None, None), width=500)

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required
        # to contain all the childs. (otherwise, we'll child outside the
        # bounding box of the childs)
        layout.bind(minimum_height=layout.setter('height'))

        # add button into that grid
        for i in range(30):
            label = Label(text=str(i), size=(480, 20),
                         size_hint=(None, None), color=[105, 106, 188, 1])
            layout.add_widget(label)

        # create a scroll view, with a size < size of the grid
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                pos_hint={'x': 0, 'center_y': .5}, do_scroll_x=False)
        root.add_widget(layout)

        return root


if __name__ == '__main__':

    ScrollViewApp().run()
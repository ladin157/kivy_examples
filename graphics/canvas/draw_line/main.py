# kivy Lines Demo
# ref: https://www.geeksforgeeks.org/python-line-canvas-in-kivy/
# https://www.geeksforgeeks.org/kivy-tutorial/

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# Widgets are elements of
# a graphical user interface that
# form part of the User Experience.
from kivy.uix.widget import Widget


##############################################
# Classes form Different types of line as  widgets

class LineEllipse1(Widget):
    pass


class LineEllipse2(Widget):
    pass


class LineEllipse3(Widget):
    pass


class LineCircle1(Widget):
    pass


class LineCircle2(Widget):
    pass


class LineCircle3(Widget):
    pass


class LineCircle4(Widget):
    pass


class LineRectangle(Widget):
    pass


class LineBezier(Widget):
    pass


# Create the App class
class LineApp(App):
    def build(self):
        # Assign the number of coloumn, spacing and padding
        root = GridLayout(cols=3, padding=50, spacing=100)

        # Adding the widgets
        root.add_widget(LineEllipse1())
        root.add_widget(LineEllipse2())
        root.add_widget(LineEllipse3())
        root.add_widget(LineCircle1())
        root.add_widget(LineCircle2())
        root.add_widget(LineCircle3())
        root.add_widget(LineCircle4())
        root.add_widget(LineRectangle())
        root.add_widget(LineBezier())
        return root

    # Run the App class


if __name__ == '__main__':
    LineApp().run()

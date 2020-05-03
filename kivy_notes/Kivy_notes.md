Kivy Notes
-----------------------

# 1. Screen Manager:
The screen manager is a widget dedicated to managing multiple screens for your application.
The default ScreenManager __displays only one Screen at a time__ and uses TrasitionBase to switch from one Screen to another.
Multiple transitions are supported based on changing the screen coordinates/scale or even performing fancy animatin using custom shaders.

Screen <-- RelativeLayout.
## Events:
1. on_pre_enter
2. on_enter
3. on_pre_enter
4. on_pre_leave
5. on_leave
## Properties:
1. manager
2. name
3. transition_progress
4. transition_state

## ScreenManager
### Events & properties
1. add_widget
2. clear_widgets
3. current
4. current_screen
5. get_screen
6. has_screen
7. next
8. on_touch_down(touch)
9. on_touch_move(touch)
10. on_touch_up(touch)
11. previous
12. remove_widget(*|)
13. screen_names
14. screens
15. switch_to(screen, **options)
16. transition

**Some classes**:
1. ScreenManagerException
2. TransitionBase
3. ShaderTransition
4. SlideTransition
5. SwapTransition
6. FadeTransition
7. WipeTransition
8. FallOutTransition
9. RiseInTransition
10. NoTransition
11. CardTransition


**BASIC USAGE**:
- When you are creating a screen, you absolutely need to give a name to it.
``` Python
from kivy.uix.screenmanager import ScreenManager, Screen


# Create the manager
sm = ScreenManager()

# Add few screens
for i in range(4):
    screen = Screen(name='Title %d' % i)
    sm.add_widget(screen)

# By default, the first screen added into the ScreenManager will be
# displayed. You can then change to another screen.

# Let's display the screen named 'Title 2'
# A transition will automatically be used.
sm.current = 'Title 2'
```

# 2. Clock
The Clock object allows you to schedule a function call in the future; once or repeatedly at specified intervals. You can get the time elapsed between the scheduling and the calling of the callback via the dt argument.

``` Python
# dt means delta-time
def my_callback(dt):
    pass

# call my_callback every 0.5 seconds
Clock.schedule_interval(my_callback, 0.5)

# call my_callback in 5 seconds
Clock.schedule_once(my_callback, 5)

# call my_callback as soon as possible (usually next frame.)
Clock.schedule_once(my_callback)

```

# 3. Kivy Language
Ref: https://kivy.org/doc/stable/api-kivy.lang.html
The Kivy language is a language dedicated to describing user interface and interactions.
The language consists of several constructs that we can see:
- Rules
- A Roolt Widget
- Dynamic Classes
- Templates (deprecated)

# 4. Properties
Ref: https://kivy.org/doc/stable/api-kivy.properties.html
The Properties classes are used when you created an EventDispatcher.
It supports:
- Value Checking / Validation
- Observer Pattern
- Better Memory Management

Properties can:
- Observe Property changes
- Binding to properties of properties

Classes:
- Property
- NumericProperty
- StringProperty
- ListProperty
- ObjectProperty
- BooleanProperty
- BoundedNumericProperty
- OptionProperty
- ReferenceListProperty
- AliasProperty
- DictProperty
- VariableListProperty
- ConfigParserProperty

# 5. Widget interactions between Python and KV
Ref: https://blog.kivy.org/2019/06/widget-interactions-between-python-and-kv/

1. Option 1: ids
2. Option 2: properties
3. The parent and children properties

# 6. Kv Language
## Concept behind the language:
Application grows more complex --> difficult to maintain --> KV language.
## Load Kv
- Naming
- Builder:
    + Load file
    + Load string
## Rule Context
- app
- root
- self
## Special syntax
```Python
#:import isdir os.path.isdir
#:import np numpy
```
## Instantiate children
## Event Bindings
## Extend canvas
## Referencing Widgets
Example:
```Python
<MyWidget>:
    label_widget: label_widget
    Button:
        text: 'Add Button'
        on_press: root.add_widget(label_widget)
    Button:
        text: 'Remove Button'
        on_press: root.remove_widget(label_widget)
    Label:
        id: label_widget
        text: 'widget'
```
To keep the widget alive, a direct reference to the label_widget widget must be kept. This is achieved using id.__self__ or label_widget.__self__ in this case. The correct way to do this would be:

```Python
<MyWidget>:
    label_widget: label_widget.__self__
```    
    
    
## Access Widgets define in Kv lang in Python code
- Properties
- ids

## Dynamic Classes

## Reusing styles in multiple widgets

## Designing with the Kivy language
One of aims of the Kivy language is to separate the concerns of presentation and logic. 

The presentation (layout) side is addressed by your kv file and the logic by .py file.

# Graphics
Canvas:
- context instructions
- vertext interactions

## Context instructions:
Context instructions manipulate opengl context. You can rotate, translate, and scale your canvas. You can also attach a texture or change the drawing color.

This one is the most commonly used, but others are really useful too:
```
with self.canvas.before:
    Color(1, 0, .4, mode='rgb')
```
## Drawing instructions
```
with self.canvas:
   # draw a line using the default color
   Line(points=(x1, y1, x2, y2, x3, y3))

   # lets draw a semi-transparent red square
   Color(1, 0, 0, .5, mode='rgba')
   Rectangle(pos=self.pos, size=self.size)
```







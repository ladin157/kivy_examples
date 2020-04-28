from kivy.uix.modalview import ModalView
from kivy.uix.selectableview import SelectableView
from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.app import App


# For some reason, size_hint_y and height set here have no effect.
# See list_kv.py for some difference that matters, as it works there.
#
#     Note: The reference in the kv definition to this list item args
#           converter function looks a bit odd -- it is because of the
#           need to reference the current module. Maybe there is a
#           better way?
def list_item_args_converter(row_index, text):
    return {'text': text,
            'size_hint_y': None,
            'height': 70}


Factory.register('BoxLayout', cls=BoxLayout)
Factory.register('SelectableView', cls=SelectableView)
Factory.register('ListItemButton', cls=ListItemButton)

# Note the special nature of indentation in the adapter declaration, where
# the adapter: is on one line, then the value side must be given at one level
# of indentation.

Builder.load_string("""
#:import sys sys
#:import lv kivy.uix.listview
#:import la kivy.adapters.listadapter
[CustomListItem@SelectableView+BoxLayout]:
    size_hint: None, None
    height: 70
    width: 400
    ListItemButton:
        text: ctx.text
        font_size: '40sp'
<ListViewModal>:
    list_view: list_view_id
    GridLayout:
        cols: 1
        size_hint: 1, 1
        ListView:
            id: list_view_id
            adapter:
                la.ListAdapter(
                data=["Item #{0}".format(i) for i in xrange(100)],
                selection_mode='single',
                allow_empty_selection=False,
                list_item_args_converter=sys.modules['__main__'].list_item_args_converter,
                template='CustomListItem')
""")


class ListViewModal(ModalView):
    selected_item = StringProperty('no selection')

    def __init__(self, **kwargs):
        super(ListViewModal, self).__init__(**kwargs)
        self.list_view.adapter.bind(on_selection_change=self.selection_changed)

    # This is for the binding set up at instantiation, to the list adapter's
    # special on_selection_change (bind to it, not to adapter.seleciton).
    def selection_changed(self, *args):
        print('    args when selection changes gets you the adapter', args)
        self.selected_item = args[0].selection[0].text

    # This is to illustrate another type of binding. This time it is to this
    # class's selected_item StringProperty (where the selected item text is set).
    # See other examples of how bindings are set up between things. This one
    # works because if you put on_ in front of a Kivy property name, a binding
    # is set up for you automatically.
    def on_selected_item(self, *args):
        print('    args when a list property changes gets you the list property, and the changed item', args)
        print('selected item text', args[1])


class MainView(BoxLayout):
    """
    Implementation of a ListView using the kv language.
    """

    def __init__(self, **kwargs):
        kwargs['orientation'] = 'vertical'
        kwargs['size_hint'] = (1.0, 1.0)
        super(MainView, self).__init__(**kwargs)

        listview_modal = ListViewModal()

        self.add_widget(listview_modal)


class MyApp(App):
    def build(self):
        return MainView(width=800)


MyApp().run()

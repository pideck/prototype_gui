from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.selectableview import SelectableView
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.button import ButtonBehavior


Builder.load_string('''
<TrackItem>:
    cols: 1
    Button:
        text: root.title
    Label:
        text: root.title
        width: self.texture_size[0]
        font_size: sp(16)
        size_hint_x: None
        color: [1, 1, 1, 1]
''')


class TrackData(object):
    def __init__(self, title='Track Data Title', is_selected=False):
        self.title = title
        self.is_selected = is_selected


class TrackItem(ButtonBehavior, GridLayout, SelectableView):
    title = StringProperty('Default Title')
    is_selected = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super(TrackItem, self).__init__(**kwargs)

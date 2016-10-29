from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<PlaylistView>:
    Button:
        text: 'PlaylistView'
''')


class PlaylistView(BoxLayout):
    pass

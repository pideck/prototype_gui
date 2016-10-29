from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<PlayingView>:
    Button:
        text: 'PlayingView'
''')


class PlayingView(BoxLayout):
    pass

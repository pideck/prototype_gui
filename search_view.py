from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<SearchView>:
    Button:
        text: 'Text'
''')


class SearchView(BoxLayout):
    pass

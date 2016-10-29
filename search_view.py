from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string('''
<SearchView>:
    Button:
        text: 'SearchView'
''')


class SearchView(BoxLayout):
    pass

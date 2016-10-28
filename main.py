from kivy.config import Config
# Resize the Window for the Desktop Environment
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


from kivy.app import App
from kivy.uix.pagelayout import PageLayout


# Root Widget
class Prototype(PageLayout):
    pass


class PrototypeApp(App):
    def build(self):
        return Prototype()


if __name__ == '__main__':
    PrototypeApp().run()

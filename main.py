from kivy.config import Config
# Resize the Window for the Desktop Environment
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')


from kivy.app import App
from kivy.uix.widget import Widget


# Root Widget
class Prototype(Widget):
    pass


class PrototypeApp(App):
    def build(self):
        return Prototype()


if __name__ == '__main__':
    PrototypeApp().run()

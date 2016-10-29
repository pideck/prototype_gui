from kivy.config import Config
# Resize the Window for the Desktop Environment
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.factory import Factory
from kivy.uix.listview import ListView
from kivy.adapters.listadapter import ListAdapter
from track import TrackData
from track import TrackItem


# Root Widget
class Prototype(PageLayout):
    pass


class TrackListView(ListView):
    
    def __init__(self, **kwargs):
        super(TrackListView, self).__init__(**kwargs)
        
        def converter(row_index, obj):
            return {'title': obj.title}
        
        self.adapter = ListAdapter(data=[],
                                   args_converter=converter,
                                   propagate_selection_to_data=True,
                                   selection_mode='multiple',
                                   cls=TrackItem)
        self.adapter.data = self.generate_pseudo_data()
    
    def generate_pseudo_data(self):
        data_items = []
        for i in range(0, 3):
            data_items.append(TrackData())
        return data_items


class PrototypeApp(App):
    Factory.register('SearchView', module='search_view')
    Factory.register('PlaylistView', module='playlist_view')
    Factory.register('PlayingView', module='playing_view')
    
    def build(self):
        return Prototype()


if __name__ == '__main__':
    PrototypeApp().run()

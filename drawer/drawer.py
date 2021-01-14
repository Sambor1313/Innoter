from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ListProperty, ObjectProperty, StringProperty, ColorProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.colorpicker import ColorWheel

from kivy.graphics import Color, Ellipse, Line


class DrawerScreen(Screen, Widget):
    mode_tool = NumericProperty(0)
    obk = ObjectProperty(None)
    title = StringProperty(None)
    label = ColorProperty(None)

    def on_enter(self):
        file_path = self.manager.screens[2].open_file
        self.obk = Object_keeper()
        if file_path:
            self.obk.load_parser(file_path)
        else:
            self.obk.load_parser()

        self.title = self.obk.settings['title']
        self.label = self.obk.settings['label']

        # for obk.settings[]
        # self.obk.save_parser()

    def on_touch_down(self, touch):
        color = (1, 0, 0)
        print(touch.button)
        with self.canvas:
            Color(*color)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        print("Analise")


class Object_keeper():
    settings = []  # ListProperty(None)
    objects = []  # ListProperty(None)
    store = None

    def load_parser(self, file='./saves/default.json'):
        print("Parsing save:", file)
        self.store = JsonStore(file)
        self.settings = self.store.get('settings')
        self.objects = self.store.get('objects')

    def save_parser(self):
        self.store.put('settings',
                       title='PFf',
                       )


class ModeTool(Widget):
    pass


class Paper(ScrollView):
    pass

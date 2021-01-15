from kivy.graphics import Color, Ellipse, Line
from kivy.uix.colorpicker import ColorWheel
from kivy.storage.jsonstore import JsonStore
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.properties import (NumericProperty,
                             ListProperty,
                             ObjectProperty,
                             StringProperty,
                             ColorProperty,
                             BoundedNumericProperty,
                             DictProperty
                             )


class TopBar(GridLayout):
    def file_button(self):
        print("File")

    def save_button(self):
        print("Save")

    def name_button(self):
        print("Change Name")


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


class ModeTool(GridLayout):
    mode = NumericProperty(0)

    def get_mode(self):
        return mode

    def set_mode(self, value):
        self.mode = value


class MLTool(GridLayout):
    lvl = BoundedNumericProperty(0, min=0, max=3)

    def get_lvl(self):
        return self.lvl

    def set_lvl(self, value):
        self.lvl = value

    def up_lvl(self):
        try:
            self.lvl = self.lvl + 1
        except ValueError as ve:
            # Idea: Open window to let know 3 is max
            pass

    def down_lvl(self):
        try:
            self.lvl = self.lvl - 1
        except ValueError as ve:
            # Idea: Open window to let know 0 is min
            pass


class StyleManager(FloatLayout):
    option_selected = BoundedNumericProperty(0, min=0, max=2)
    option_sets = DictProperty({'lines': [{'a': "-1", 'b': "-2"}]})
    l1 = ObjectProperty(Line(points=(0, 80, 80, 80)))

    def collect_option(self, options):
        self.option_sets = options
        print(self.option_sets)

    def get_option_set(self):
        return self.option_sets[self.option_selected]


class Paper(FloatLayout):

    def on_touch_down(self, touch):
        color = (0, 0, 0, .8)
        print(touch.button)
        if touch.button == 'left':
            with self.canvas:
                Color(*color)
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)
        elif touch.button == 'middle':
            pass

    def on_touch_move(self, touch):
        if touch.button == 'left':
            touch.ud['line'].points += [touch.x, touch.y]
        elif touch.button == 'middle':
            pass  # sefl.parent()

    def on_touch_up(self, touch):
        return
        if touch.button == 'left':
            print("Line lenght:", len(touch.ud['line'].points))
        elif touch.button == 'middle':
            pass


class TableWorkspace(ScrollView):
    paper = ObjectProperty(Paper())
    pass
    # def on_touch_down(self, touch):
    #     if touch.button == "middle":
    #         print("Scroll - middle")
    #         super(ScrollView, self).on_touch_down(touch)
    #         return True


class DrawerScreen(Screen, Widget):
    obk = ObjectProperty(None)
    title = StringProperty(None)
    label = ColorProperty(None)
    top_bar = ObjectProperty(TopBar())
    mode_tool = ObjectProperty(ModeTool())
    ml_tool = ObjectProperty(MLTool())
    table_workspace = ObjectProperty(TableWorkspace())
    style_manager = ObjectProperty(StyleManager())

    def on_enter(self):
        file_path = self.manager.screens[2].open_file
        self.obk = Object_keeper()
        if file_path:
            self.obk.load_parser(file_path)
        else:
            self.obk.load_parser()

        self.title = self.obk.settings['title']
        self.label = self.obk.settings['label']

        self.style_manager.collect_option(self.obk.settings['styles'])
        pass
        # for obk.settings[]
        # self.obk.save_parser()

#####################
# Utils


class NameLabel(Label):
    pass

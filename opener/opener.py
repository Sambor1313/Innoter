from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.properties import ListProperty, ObjectProperty, StringProperty


class LoadDialog(FileChooserIconView):

    files = ListProperty(['\*.json'])

    def on_submit(self, selection, touch):
        self.parent.parent.parent.dismiss()


class OpenerScreen(Screen, Widget):
    open_file = StringProperty(None)
    pop_window = ObjectProperty(None)
    loading_to_show = LoadDialog()

    def show_file_loader(self, *args, **kwargs):
        #loading_to_show = LoadDialog()
        pop_window = Popup(title="Choose file to load",
                           content=self.loading_to_show)
        pop_window.open()
        self.loading_to_show.bind(on_submit=self.to_draw)

    def to_draw(self, *args, **kwargs):
        """
        docstring
        """
        open_file = self.loading_to_show.selection[0]
        self.manager.screens[2].open_file = self.loading_to_show.selection[0]
        print("Man:", self.manager.screens[2].open_file)
        self.manager.current = 'draw'

    def on_pre_leave(self):
        """
        Refactoring idea for opener
        """
        pass
        #print("Pre leave Opener")

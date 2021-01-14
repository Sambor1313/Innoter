from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

from welcome.welcome import *
from opener.opener import *
from drawer.drawer import *

# Builder.load_file("welcome/welcomescreen.kv")
Config.set('graphics', 'resizable', True)


class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(DrawerScreen(name='draw'))
        sm.add_widget(OpenerScreen(name='open'))
        return sm


if __name__ == '__main__':
    Builder.load_file("welcome/welcomescreen.kv")
    Builder.load_file("opener/opener.kv")
    Builder.load_file("drawer/drawerscreen.kv")
    MainApp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmangaer import ScreenManager, Screen

Builder.load_file('design.kv')


class LoginScreen(Screen):
    pass

# template for every app screen


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):

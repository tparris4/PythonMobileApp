from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.gridlayout import GridLayout
# dir(GridLayout)
Builder.load_file('design.kv')


class LoginScreen(Screen):
    pass

# template for every app screen


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()

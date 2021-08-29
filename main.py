from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import glob
from datetime import datetime
from pathlib import Path
# from kivy.uix.gridlayout import GridLayout
# dir(GridLayout)
Builder.load_file('design.kv')

# loginscreen is referring to login screen in kv file
# we access it through login screen class
# self is pointing to login screen class


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] = pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password"


# template for every app screen


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            user = json.load(file)
        print(users)

        users[uname] = {'username': uname, 'password': pword,
                        'created': datetime.now().strttime("%Y-%m-%d-%H-%M-%S")}
        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def go_to_login(self):

        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.globa("quotes/*txt")
        print(available_feelings)
        # extract names of the files


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()

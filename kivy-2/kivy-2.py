#! /usr/bin/env python3

import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Authentication:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)

class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    # don't forget () after SimpleKivy
    # (this creates an instance
    # of the SimpleKivy class)
    SimpleKivy().run()

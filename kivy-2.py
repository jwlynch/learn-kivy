#! /usr/bin/env python3

import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        pass

class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    # don't forget () after SimpleKivy
    # (this creates an instance
    # of the SimpleKivy class)
    SimpleKivy().run()

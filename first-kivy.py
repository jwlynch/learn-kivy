#! /usr/bin/env python3

import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.uix.label import Label

class SimpleKivy(App):
    pass

if __name__ == "__main__":
    # don't forget () after SimpleKivy
    # (this creates an instance
    # of the SimpleKivy class)
    SimpleKivy().run()

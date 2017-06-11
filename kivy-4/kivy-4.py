#! /usr/bin/env python3

#import kivy
#kivy.require("1.8.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass

class SimpleKivy(App):
    def build(self):
        return Label()

if __name__ == "__main__":
    # don't forget () after SimpleKivy
    # (this creates an instance
    # of the SimpleKivy class)
    SimpleKivy().run()

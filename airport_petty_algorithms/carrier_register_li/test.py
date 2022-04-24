import kivy
# from kivy.app import App
from kivymd.app import MDApp

from kivy.uix.button import (
    Button,
)

from kivy.uix.label import (
    Label,
)

from kivy.uix.textinput import (
    TextInput,
)

from kivy.graphics import (
    Color,
    Rectangle, 
    RoundedRectangle,
    Ellipse
)

from kivy.properties import (
    NumericProperty, 
    StringProperty, 
    ObjectProperty
)

from parse_data import (
    FuelArrivedValidation,
    FuelResidueValidation,
    ParseXLSXData
)

from kivymd.uix.picker import MDDatePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.button import (
    MDFloatingActionButton,
    MDRaisedButton
)

from kivy.properties import ObjectProperty
from kivy.uix.filechooser import (
    FileChooserIconView,
    FileChooserListView
)


import datetime

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.factory import Factory

### *** Layouts *** ###

from kivy.uix.image import AsyncImage
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.clock import Clock

### time ###
import time

### encoding ###
import hashlib
import hmac
import os

import os

class FileChooserLayout(Widget):

    def select(self, filename, *args):
        self.ids.my_file._source = filename[0]
        self.file_name = filename[0]
    
    def get_file(self, filename):
        download_path = f"This is path: {self.file_name}"
        print(download_path)


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def select(self, filename, *args):
        
        # print(filename)
        # print(self.ids.my_file.source)
        self.ids.my_file._source = filename[0]
        # print(filename[0])
        # print(dir(Widget))
        self.file_name = filename[0]
        # print(type(self.file_name))

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class Editor(MDApp):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Editor().run()
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

from kivy.config import Config
Config.set('graphics', 'resizable', True)
kivy.require('2.1.0')

import os


class DialogBox(Popup):
    
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(DialogBox, self).__init__(**kwargs)

        with self.canvas.before:
            self.size = (400, 200)
            self.pos=(200, 350)

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        # print(instance.pos)
        self.pos = instance.pos
        self.size = instance.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dismiss()
            DialogBox.active = None
            return True
        return super(DialogBox, self).on_touch_down(touch)

class LoadDialog(Widget):

    title = ""
    def __init__(self, title=title, *args, **kwargs):
        self.title=title,
        # make sure we aren't overriding any important functionality
        super(LoadDialog, self).__init__(*args, **kwargs)
    
    def select(self, filename, *args):
        self.ids.my_file._source = filename[0]
        self.file_name = filename[0]
        print(f"FINAL: {self.file_name} - TITLE: {self.title}")
        print("#2")

    def process_final(self):
        self.message = f"{self.file_name}"
        content=Label(text=self.message)
    
        self._popup = DialogBox(
            title="Final File Selected",
            title_size="25sp",
            text_size="45sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=True,
            )
        ### print(content.text) +++
        self._popup.open()
        self.clear_widgets()
    
    def new_layer(self, instance=None):
        self.message = f"{self.file_name}"
        content=Label(text=self.message)
    
        self._popup = DialogBox(
            title="Final File Selected",
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=True,
            )

        self._popup.open()
        self.clear_widgets()
        
        widget = MainPage()
        self.add_widget(widget)
        


class MainPage(Widget):

    rt_image_path = '/media/netunit/storage/SoftServeItAcademy/' \
        + 'airport_petty_algorithms/carrier_register_li/rt-sticker-280-x-75mm.jpg'
    jet_image_path = '/media/netunit/storage/SoftServeItAcademy/' \
        + 'airport_petty_algorithms/carrier_register_li/jet-a-1-sticker-280-x-75mm.jpg'
    ### *** FUEL_TYPE *** ###
    def select_fuel(self, fueltype, *args):
        if not fueltype == 'Jet A-1':
            self.ids.my_image.source = self.rt_image_path
        else:
            self.ids.my_image.source = self.jet_image_path

        self.ids.fuel_selection._source = fueltype
            
        self.fuel_type = fueltype
        self.message = f"{self.fuel_type}"
        
        self._popup = DialogBox(
            title=u'\u274C' + f'  Fuel Selected',
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=False,
            )
        
        self._popup.open()

    def process(self):
        print('This is process')

class Root(Widget):

    def dismiss_popup(self):
        self._popup.dismiss()

    def select(self, filename, *args):
        self.ids.my_file._source = filename[0]
        self.file_name = filename[0]
        print(f"INITIAL: {self.file_name}")
        
    def process_initial(self):
        print('#1')
        widget = LoadDialog()
        self.add_widget(widget)
        ### *** change this later <-- LoadDialog with *par *** ###
        self.message = f"{self.file_name}"
        content=Label(text=self.message)

        self._popup = DialogBox(
            title="Initial File Selected",
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=True,
            )
        self._popup.open()
        ### print(content.text) +++
        ### *** change this later <-- LoadDialog with *par *** ###
        # self.clear_widgets()
        self.show_load()
    
    def show_load(self):
        self.clear_widgets()
        widget = LoadDialog()
        self.add_widget(widget)
        


class Editor2(MDApp):
    pass


Factory.register('Root', cls=Root)
# Factory.register('FileChooserLayer', cls=FileChooserLayer)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('MainPage', cls=MainPage)
# Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Editor2().run()
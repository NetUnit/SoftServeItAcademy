import kivy
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

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

from kivymd.uix.picker import MDDatePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.button import (
    MDFloatingActionButton,
    MDRaisedButton,
    MDIconButton
)

from kivy.properties import (
    ObjectProperty,
    StringProperty
)

from kivy.uix.filechooser import (
    FileChooserIconView,
    FileChooserListView
)

# *** Layouts *** #
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.factory import Factory

from kivy.uix.image import (
    AsyncImage,
    Image
)

from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.clock import Clock
from matplotlib import cm

# *** time *** #
import time
import datetime

# *** encoding *** #
import hashlib
import hmac

# *** path *** #
from settings import (
    PathFinder,
    RT_STICKER,
    JET_STICKER,
    CLOCK_IMAGE,
    TANK_IMAGE,
)
import os

# *** COLORS *** #
from settings import (
    WHITE,
    SIGNAL_WHITE,
    PURE_WHITE,
    TRAFFIC_GREY,
    MINT_GREEN,
    BLACK,
    ASDA_GREEN,
    FOX_RED
)


kivy.require('2.1.0')
from kivy.config import Config
from configparser import ConfigParser
import configparser

# non-resizable window config 
# Config.set('graphics', 'resizable', '0')
# Config.set('graphics', 'width', '800')
# Config.set('graphics', 'height', '600')

# resizable window config
config = ConfigParser()

# parse existing file
config.read('config.ini')

# read values from a section
resizable_val = config.get('graphics', 'resizable')
debug_lvl = config.get('kivy', 'log_level')
print(debug_lvl)
Config.set('graphics', 'resizable', resizable_val)
Config.set('kivy', 'log_level', debug_lvl)
Config.write()

import re
import random
# *** root files *** #
from parse_data import ParseXLSXData
from validators.file_field import LoadXLSXFileField
from validators.supply_fields import FuelSupplyField 

# *** path *** #
CWD = PathFinder().cwd


class DialogBox(Popup):

    def __init__(self, **kwargs):
        # prevention of overriding any important functionality
        super(DialogBox, self).__init__(**kwargs)

        with self.canvas.before:
            self.size = (400, 200)
            self.pos = (200, 350)
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.pos = instance.pos
        self.size = instance.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.dismiss()
            DialogBox.active = None
            return True
        return super(DialogBox, self).on_touch_down(touch)

    def close_app(self, touch):
        if self.collide_point(*touch.pos):
            self.dismiss()
            DialogBox.active = None
            Editor.get_running_app().stop()


class CustomDialog(FloatLayout):

    confirm = ObjectProperty(None)
    cancel = ObjectProperty(None)
    text = ObjectProperty(None)

    def __init__(self, confirm=confirm, **kwargs):
        self.confirm = confirm
    # prevention of overriding any important functionality
        super(CustomDialog, self).__init__(**kwargs)

        self.submit_btn = MDRaisedButton(
            text="Confirm",
            # size_hint=(.1, .05),
            pos_hint={'center_x': .35, 'center_y': .15},
            md_bg_color=ASDA_GREEN,
            text_color=WHITE,
            # on_release=self.confirm
        )

        self.cancel_btn = MDRaisedButton(
            text="Cancel",
            # size_hint=(.1, .05),
            pos_hint={'center_x': .65, 'center_y': .15},
            md_bg_color=FOX_RED,
            text_color=WHITE,
        )

        self.message = Label(
            text=self.text,
            pos_hint={'center_x': .5, 'center_y': .75},
            # pos=(150.0, 80.0)
        )

        self.add_widget(self.submit_btn)
        self.add_widget(self.cancel_btn)
        self.add_widget(self.message)

        # self.confirm is an obj par that will be
        # acquired in the other class - function which
        # is basically a python object too
        self.submit_btn.bind(on_press=self.confirm)
        self.cancel_btn.bind(on_press=self.cancel)


class SoundButtonCard(BoxLayout):

    app_name = 'Carrier Register'
    music_dir = f'{CWD}/'
    counter = 0

    def __init__(self, *args, **kwargs):
        # prevention of overriding any important functionality
        super(SoundButtonCard, self).__init__(*args, **kwargs)

        # dir songs related values
        self.music_files = os.listdir(self.music_dir)
        self.song_list = [i for i in self.music_files if i.endswith(('mp3'))]
        self.song_count = len(self.song_list)

    def playaudio(self):
        double_click = self.counter == 1

        if not double_click:
            self.song_title = self.song_list[
                random.randrange(0, self.song_count)
            ]
            self.sound = SoundLoader.load(f"{self.music_dir}{self.song_title}")
            self.sound.play()
            self.counter += 1

    def stopaudio(self):
            self.sound.stop()
            self.counter -= 1


class Root(Widget):
    
    def __init__(self, *args, **kwargs):
        # prevention of overriding any important functionality
        super(Root, self).__init__(*args, **kwargs)

    def dismiss_popup(self):
        self._popup.dismiss()

    def select(self, filename, *args):
        self.ids.my_file._source = filename[0]
        self.file_name = filename[0]
        msg = f"INITIAL FILE: {self.file_name} - SELECTED"
        # LOGGER.info(msg)
        print(msg)

    def process_initial(self, instance=None):
        # downloading and selection widget
        widget = ProcessFinalFile()
        self.add_widget(widget)

        path = self.ids.my_file._source
        file_name = os.path.basename(path)
        file = LoadXLSXFileField(path, file_name)

        global path_initial
        full_path = file.path
        path_initial = os.path.dirname(full_path)

        global registry
        registry = file.file_name

        err_free = file.err is None
        # print(file.err)
        if err_free:
            title = "Initial File Selected"
            self.message = f"{self.file_name}"
        else:
            self.file_name = str(instance)
            title = "Initial File Error"
            self.message = file.err

        msg = f"INITIAL FILE: {self.file_name} - PROCESSED"
        # LOGGER.info(msg)
        print(msg)
        content = Label(text=self.message)

        self._popup = DialogBox(
            title=title,
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=True,
            )
        if not err_free:
            self._popup.on_touch_down = self._popup.close_app

        self._popup.open()
        self.show_load()

    def show_load(self):
        self.clear_widgets()
        widget = ProcessFinalFile()
        self.add_widget(widget)


class ProcessFinalFile(Widget):

    path = StringProperty("")
    report = StringProperty("")
    title = ""

    def __init__(self, title=title, *args, **kwargs):
        self.title = title,
        # preventionof overriding any important functionality
        super(ProcessFinalFile, self).__init__(*args, **kwargs)
    
    def select(self, filename, *args):
        self.ids.my_file._source = filename[0]
        self.file_name = filename[0]
        # LOGGER.info(msg)
        msg = f"FINAL FILE: {self.file_name} - SELECTED"
        print(msg)

    def process_final(self, instance=None):
        # print(instance)
        path = self.ids.my_file._source
        file_name = os.path.basename(path)

        # file obj validation
        file = LoadXLSXFileField(path, file_name)
        global path_final
        full_path = file.path
        path_final = os.path.dirname(full_path)

        global report
        report = file.file_name

        # in case of field error
        err_free = file.err is None
        if err_free:
            title = "Initial File Selected"
            self.message = f"{self.file_name}"
        else:
            self.file_name = str(instance)
            title = "Initial File Error"
            self.message = file.err

        content = Label(text=self.message)
        msg = f"FINAL FILE: {self.file_name} - PROCESSED"

        self._popup = DialogBox(
            title=title,
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=True,
            )

        if not err_free:
            self._popup.on_touch_down = self._popup.close_app

        self._popup.open()

        self.clear_widgets()
        widget = FuelSelection()
        self.add_widget(widget)


class FuelSelection(Widget):

    label_paths = {
        'RT': RT_STICKER,
        'Jet A-1': JET_STICKER,
    }

    def __init__(self, *args, **kwargs):
        # preventionof overriding any important functionality
        super(FuelSelection, self).__init__(*args, **kwargs)

    # fuel_type selection
    def select_fuel(self, fueltype):
        label_path = self.label_paths.get(fueltype)
        label_path = "" if label_path is None else label_path
        self.ids.my_image.source = label_path
        self.ids.fuel_selection._source = fueltype

        global fuel_type
        fuel_type = fueltype
        self.fuel_type = fueltype
        self.message = f"{self.fuel_type}"
        return fuel_type

    def process_fuel_selection(self, fueltype=None):
        fuel_type = self.ids.fuel_selection._source
        # fuel_type will be blanc string if no selection
        if len(fuel_type) > 0:
            self.fuel_type = fuel_type
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
            self.clear_widgets()
            widget = DatePicker()
            self.add_widget(widget)

        # case when fuel_type wasn't selected
        else:
            self.message = 'Select Fuel First'
            self._popup = DialogBox(
                title=u'\u274C' + f'  Error',
                title_size="25sp",
                content=Label(text=self.message),
                pos=(200.0, 350.0),
                size_hint=(0.5, 0.25),
                size=(400, 200),
                auto_dismiss=False,
            )

            self._popup.open()
            self.select_fuel(fueltype=fuel_type)


class DatePicker(Widget):

    clock_image = CLOCK_IMAGE
    format = '%d-%m-%Y'

    def __init__(self, *args, **kwargs):
        # make sure we aren't overriding any important functionality
        super(DatePicker, self).__init__(*args, **kwargs)

        self.clock_image = Image(
            source=self.clock_image,
            pos=(250.0, 280.0),
            size=(300.0, 300.0),
        )
        self.add_widget(self.clock_image)

        self.clock_label = Label(
            text="Select report date",
            color=WHITE,
            pos=(350.0, 180.0),
            font_size="20dp"
        )
        self.add_widget(self.clock_label)

    def get_date_picker(self):
        self.add_widget(self.date_btn)
        self.date_btn.bind(on_press=self.show_date_picker)

    def show_date_picker(self):
        today = datetime.date.today()
        self.date_dialog = MDDatePicker(
            year=today.year,
            month=today.month,
            day=today.day
        )

        self.date_dialog.bind(
            on_save=self.date_on_save,
            on_cancel=self.date_on_cancel
            )

        self.date_dialog.open()

    def date_on_save(self, instance, value, date_range):
        self.date_dialog.dismiss()
        self.message = f'Selected date is: {value}'

        global date
        date = value

        self.date_dialog.dismiss()
        dialog = DialogBox(
            title=u'\u274C',
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=False,
            )

        dialog.open()

        self.clear_widgets()
        widget = FuelSupply()
        self.add_widget(widget)

    def date_on_cancel(self, instance, value):
        self.date = None 
        self.date_dialog.dismiss()


class FuelSupply(Widget):

    tank_image = TANK_IMAGE
    succes_msg = u"THE REPORT HAS BEEN DONE"

    def __init__(self, *args, **kwargs):
        # prevention of overriding any important functionality
        super(FuelSupply, self).__init__(*args, **kwargs)

        self.tank_image = Image(
            source=self.tank_image,
            pos=(168.0, 370.0),
            size=(465.0, 169.0),
        )
        self.add_widget(self.tank_image)

        self.pickup_lbl = MDLabel(
            pos=(45.0, 280.0),
            text="Fuel pick-up (trucks), kg",
            theme_text_color="Custom",
            text_color=WHITE,
            size=(250, 40)
            # size_hint=(0.4, 0.1),
            # halign="center",
            # pos_hint={'center_x': .95, 'center_y': .4}
        )

        self.pickup_input = TextInput(
            multiline=False,
            pos=(40.0, 250.0),
            size_hint=(.2, None),
            size=(150, 25),
            height=35.0,
            width=200.0,
            # placeholder - adjust for zoom placeholder text -->
            text=u"Самовивіз зі складу"
            # pos_hint={'center_x': .20, 'center_y': .50},
            # on_release=self.process_fuel_arrival
        )

        self.arrival_input_lbl = MDLabel(
            pos=(45.0, 200.0),
            text="Fuel arrival (trucks/rail), kg",
            theme_text_color="Custom",
            text_color=WHITE,
            size=(250, 40)
            # size_hint=(0.4, 0.1),
            # halign="center",
            # pos_hint={'center_x': .95, 'center_y': .4}
        )

        self.arrival_input = TextInput(
            multiline=False,
            pos=(40.0, 170.0),
            size_hint=(.2, None),
            size=(150, 25),
            height=35.0,
            width=200.0,
            # placeholder - adjust for zoom placeholder text -->
            text=u"Прибуток палива"
            # pos_hint={'center_x': .20, 'center_y': .50},
            # on_release=self.process_fuel_arrival
        )

        prev_rep_date = date - datetime.timedelta(days=1)
        prev_rep_date = ParseXLSXData.to_str(prev_rep_date, '%d-%m-%Y')

        self.residue_input_lbl = MDLabel(
            pos=(45.0, 120.0),
            text=f"Residue at {prev_rep_date}, kg",
            theme_text_color="Custom",
            text_color=WHITE,
            size=(250, 40)
            # size_hint=(0.4, 0.1),
            # halign="center",
            # pos_hint={'center_x': .95, 'center_y': .4}
        )

        self.residue_input = TextInput(
            multiline=False,
            pos=(40.0, 90.0),
            size_hint=(.2, None),
            size=(150, 25),
            height=35.0,
            width=200.0,
            # placeholder - adjust for zoom placeholder text -->
            text=u"Залишок на складі ПММ"
            # pos_hint={'center_x': .20, 'center_y': .50},
            # on_release=self.process_fuel_arrival
        )

        self.process_supply = MDRaisedButton(
            text="Get Report",
            # pos_hint={'center_x': .15, 'center_y': 0.75}
            pos=(40.0, 20.0),
            md_bg_color=ASDA_GREEN,
            text_color=WHITE,
            on_press=self.process_fuel_supply_data
        )

        self.add_widget(self.pickup_lbl)
        self.add_widget(self.pickup_input)

        self.add_widget(self.arrival_input_lbl)
        self.add_widget(self.arrival_input)

        self.add_widget(self.residue_input_lbl)
        self.add_widget(self.residue_input)

        # process supply inputs button confirm
        self.add_widget(self.process_supply)

    def process_fuel_supply_data(self, instance):

        global supply_form
        supply_form = FuelSupplyField(
            pickup=self.pickup_input.text,
            arrival=self.arrival_input.text,
            residue=self.residue_input.text
        )

        self.class_name = supply_form.get_classname(
            self.__class__.__name__
        ).upper()

        if supply_form.error is None:
            self.message = f"Pickup - {supply_form.pickup} kg \n" \
                + f"Arrival - {supply_form.arrival} kg \n" \
                + f"Previous day leftover - {supply_form.residue} kg"
        else:
            self.message = supply_form.error

        # Dialog inside dialog
        content = CustomDialog(
            confirm=self.confirm,
            cancel=self.cancel,
            text=self.message
        )

        # DialogBox not good because of redefined touch_down functionality
        self.dialog = Popup(
            title=u'Proceed with: ',
            title_size="25sp",
            content=content,
            pos=(200.0, 350.0),
            size_hint=(0.50, 0.50),
            size=(300, 300),
            auto_dismiss=False,
        )

        self.dialog.open()

    def cancel(self, instance):
        msg = f"{self.class_name} - OPERATION CANCELLED"
        print(msg)
        self.dialog.dismiss()

    def finalize_report(self, touch):
        if self.collide_point(*touch.pos):
            self.dismiss()
            DialogBox.active = None
            return True
        exit()

    def confirm(self, instance):
        err_free = supply_form.error is None
        if not err_free:
            msg = f"{self.class_name} - HAS BEEN FILLED IMPROPERLY"
            # LOGGER.info(msg)
            print(msg)
            exit()

        msg = f"{self.class_name} - HAS BEEN FILLED PROPERLY"
        # LOGGER.info(msg)
        print(msg)

        # instantiating parser class
        instance = ParseXLSXData(
            path_initial=path_initial,
            path_final=path_final,
            file_initial=registry,
            file_final=report,
            select_fuel=fuel_type,
            date=date,
            fuel_arrival=supply_form.arrival,
            fuel_pickup=supply_form.pickup,
            fuel_residue=supply_form.residue,
            )

        # launching parser here
        instance.submain()

        self.dialog = DialogBox(
            title=u'\u274C',
            title_size="25sp",
            content=Label(text=self.succes_msg),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=False,
            )

        self.dialog.on_touch_down = self.dialog.close_app
        self.dialog.open()


class Editor(MDApp):

    app_name = 'Carrier Register'
    _fixed_size = (800, 600)

    def build(self):
        '''
            overriding build() is an alternative to create a root widget 
            tree, in our case we've defined a root widget in a kv file
        '''
        config = self.config
        return 

    def get_fixed_size(self):
        '''
            setting window size as fixed with deafult values
            'param Window': Core class for creating the default Kivy window
        '''
        Window.size = self._fixed_size
        return 

    # adjust here to change size other than editor.kv file
    # way 1
    # Window.bind(on_resize = self.get_fixed_size)
    # way 2, simply hradcoding teh size 
    # Window.size = (800, 600)

    def get_application_name(self):
        _app_name = self.app_name
        _app_name.encode(encoding='UTF-8', errors='strict')
        return _app_name

Factory.register('Root', cls=Root)
Factory.register('ProcessFinalFile', cls=ProcessFinalFile)
Factory.register('DatePicker', cls=DatePicker)
Factory.register('FuelSupply', cls=FuelSupply)
Factory.register('SoundButtonCard', cls=SoundButtonCard)
Factory.register('FuelSelection', cls=FuelSelection)

if __name__ == '__main__':
    Editor().run()
    # print(dir(Editor))
    # print(dir(Window))
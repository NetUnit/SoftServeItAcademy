import kivy
# from kivy.app import App
from kivymd.app import MDApp

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
    MDRaisedButton
)

from kivy.properties import (
    ObjectProperty,
    StringProperty
)

from kivy.uix.filechooser import (
    FileChooserIconView,
    FileChooserListView
)

### *** Layouts *** ###
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

### time ###
import time
import datetime

###  *** encoding  *** ###
import hashlib
import hmac
import os

from kivy.config import Config
Config.set('graphics', 'resizable', True)
kivy.require('2.1.0')

import os
import re
### *** root files *** ###
from parse_data import ParseXLSXData
from validators.file_field import LoadXLSXFileField
from validators.supply_fields import FuelSupplyField 

### *** COLORS *** ###
WHITE = (255/255, 255/255, 255/255, 1)
SIGNAL_WHITE = (240/255, 240/255, 240/255, 0)
PURE_WHITE = (240/255, 240/255, 240/255, 1)
TRAFFIC_GREY = (83/255, 83/255, 83/255, 1)
MINT_GREEN = (155/255, 255/255, 152/255, 0.8)
BLACK = (0/255, 0/255, 0/255, 0.7)
ASDA_GREEN = (125/255, 194/255, 66/255, 1)
FOX_RED = (222/255, 44/255, 31/255, 1)

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

    path = StringProperty("")
    report = StringProperty("")
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

    def process_final(self, instance=None):
        #################################
        path = self.ids.my_file._source
        file_name = os.path.basename(path)
        
        # file is obj that is validated
        file = LoadXLSXFileField(path, file_name)
        global path_final
        full_path =  file.path
        path_final = os.path.dirname(full_path)
    
        global report
        report = file.file_name
        
        # in case of field error
        if file.err is None:
            title = "Final File Selected"
            self.message = f"{self.file_name}"
        else:
            title = "Final File Error"
            self.message = file.err
        content=Label(text=self.message)

        ##  create separate popups when err in another function
        self._popup = DialogBox(
            title=title,
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

    label_paths = {
        "RT": f'/media/netunit/storage/SoftServeItAcademy/' \
        + f'airport_petty_algorithms/carrier_register_li/rt-sticker-280-x-75mm.jpg',
        "Jet A-1": f'/media/netunit/storage/SoftServeItAcademy/' \
        + f'airport_petty_algorithms/carrier_register_li/jet-a-1-sticker-280-x-75mm.jpg'
    }

    def __init__(self, *args, **kwargs):
        # make sure we aren't overriding any important functionality
        super(MainPage, self).__init__(*args, **kwargs)

        self.process_selection = MDRaisedButton(
            text="Proceed",
            # pos_hint={'center_x': .15, 'center_y': 0.75}
            pos=(705.0, 050.0),
            md_bg_color=ASDA_GREEN,
            text_color=WHITE
            # on_press=self.process_fuel_selection
        )

        self.add_widget(self.process_selection)
        self.process_selection.bind(on_press=self.process_fuel_selection)
        
    ### *** FUEL_TYPE ***
    def select_fuel(self, fueltype):
        label_path = self.label_paths.get(fueltype)
        label_path = "" if label_path is None else label_path
        self.ids.my_image.source = label_path
        self.ids.fuel_selection._source = fueltype
        ##################
        global fuel_type
        fuel_type = fueltype
        self.fuel_type = fueltype  ## ----> convert to object
        ##################
        self.message = f"{self.fuel_type}"

    def process_fuel_selection(self, fueltype):
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

        # if fuel_type wasn't selected 
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
    
    clock_image_path = "/media/netunit/storage/SoftServeItAcademy/" \
        + "airport_petty_algorithms/carrier_register_li/clock5.png"
    
    format = '%d-%m-%Y'
    
    def __init__(self, *args, **kwargs):
        # make sure we aren't overriding any important functionality
        super(DatePicker, self).__init__(*args, **kwargs)
        
        self.clock_image = Image(
            source=self.clock_image_path,
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
        try:
            self.add_widget(self.date_btn)
            self.date_btn.bind(on_press=self.show_date_picker)
        except Exception as err:
            print(err)

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
        ################

        self.message = f'Selected date is: {value}'
        ##################
        global date
        # 2022-04-18
        # -- convert to 
        date = value 
        ##################

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
        # self.ids.date_label.text = 'Date Cancelled'
        ##################
        self.date = None ## ----> convert to object
        self.date_dialog.dismiss()
        ##################

class CustomDialog(FloatLayout):
    
    confirm = ObjectProperty(None)
    cancel = ObjectProperty(None)
    text = ObjectProperty(None)

    def __init__(self, confirm=confirm, **kwargs):
        self.confirm = confirm
    # make sure we aren't overriding any important functionality
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
        # basically a python object too
        self.submit_btn.bind(on_press=self.confirm)
        self.cancel_btn.bind(on_press=self.cancel)

class FuelSupply(Widget):
    
    tank_image = "/media/netunit/storage/SoftServeItAcademy/" \
        + "airport_petty_algorithms/carrier_register_li/fuel_track.png"

    def __init__(self, *args, **kwargs):
        # make sure we aren't overriding any important functionality
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
            # placeholder -->
            # text=u"Самовивіз зі складу"
            ### adjust for zoom
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
            # placeholder -->
            # text=u"Самовивіз зі складу"
            ### adjust for zoom
            # pos_hint={'center_x': .20, 'center_y': .50},
            # on_release=self.process_fuel_arrival
        )

        # print(f"{date} This is date")
        # date = datetime.date.today()
        # print(type(date))
        ### date is <class 'datetime.date'>

        prev_rep_date =  date - datetime.timedelta(days=1)
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
            # placeholder -->
            # text=u"Самовивіз зі складу"
            ### adjust for zoom
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
        
        ## button
        self.add_widget(self.process_supply)

    def cancel(self, instance):
        print('This is not Cancel')
        self.dialog.dismiss()
    
    def confirm(self, instance):
        if supply_form.error is None:
            print('It is Okkk')
            #### **** TESTING SUBMAIN **** ####
            instance = ParseXLSXData(
                path_initial=path_initial, ## +
                path_final=path_final, ## +
                file_initial=registry, ## +
                file_final=report, ## +
                select_fuel=fuel_type, ## +++
                date=date, ## +
                fuel_arrival=supply_form.arrival, ## +
                fuel_pickup=supply_form.pickup,  ## + 
                fuel_residue=supply_form.residue, ## +
                )
            
            print(instance.__dict__)
            
            instance.submain()

            return print('It is OK')
        else:
            exit()

    def process_fuel_supply_data(self, instance):
        #######################*** form validation *** #####################################
        global supply_form
        supply_form  = FuelSupplyField(
            pickup=self.pickup_input.text,
            arrival=self.arrival_input.text,
            residue=self.residue_input.text
        )

        if supply_form.error is None:
            self.message = f"Pickup - {supply_form.pickup} kg \n" \
                + f"Arrival - {supply_form.arrival} kg \n" \
                + f"Previous day leftover - {supply_form.residue} kg"
        else:
            self.message = supply_form.error
            
        ################################################################
        ## Dialog inside Dialog
        content = CustomDialog(confirm=self.confirm, cancel=self.cancel, text=self.message)

        # DialogBox not good because of touch_down        
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

class Root(Widget):

    # path = StringProperty("")
    # registry = StringProperty("")
    def on_icon(self):
        self.songLabel = Label(
            pos_hint={'center_x': 0.9, 'center_y': 0.05 },
            size_hint=(1, 1),
            font_size=18
        )
        self.add_widget(self.songLabel)
    
    def play_audio(self):
        

    def dismiss_popup(self):
        self._popup.dismiss()

    def select(self, filename, *args):
        self.ids.my_file._source = filename[0]
        self.file_name = filename[0]
        print(f"INITIAL: {self.file_name}")
        

    def process_initial(self):
        print('#1')
        # downloading and selection widget
        widget = LoadDialog()
        self.add_widget(widget)
        #################################
        # full_path = self.ids.my_file._source
        # file_name = os.path.basename(path)
        
        # path = full_path.split('/')[:-1]
        # path = "/".join(path) + '/'

        # # file is obj that is validated
        # file = LoadXLSXFileField(path, file_name)

        # global path_final
        # path_final = file.path
        
        # global report
        # report = file.file_name    
        
        # print(f"This is path final: {path_final}")
        # print(f"This is file final: {reportl}")
        ###############################################
        path = self.ids.my_file._source
        # print(f"This is path: {path}")
        file_name = os.path.basename(path)
        # print(f"This is filename: {file_name}")
        
        # file is obj that is validated
        file = LoadXLSXFileField(path, file_name)
        global path_initial
        full_path =  file.path
        path_initial = os.path.dirname(full_path)
        # print(f"This is path: {path_initial}")
        global registry
        registry = file.file_name

        ##################################
        if file.err is None:
            title = "Initial File Selected"
            self.message = f"{self.file_name}"
        else:
            title = "Initial File Error"
            self.message = file.err
        content=Label(text=self.message)
        ##################################
        self._popup = DialogBox(
            title=title,
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=True,
            )
        self._popup.open()
        ### print(content.text) +++
        # if file.err is None: ### ---> put condition here
        self.show_load()
    
    def show_load(self):
        self.clear_widgets()
        #######################
        # widget = FuelSupply()
        #######################
        widget = LoadDialog()
        self.add_widget(widget)
        
class Editor4(MDApp):
    
    app_name = 'Carrier Register'

    def get_application_name(self):
        _app_name = self.app_name
        _app_name.encode(encoding = 'UTF-8', errors = 'strict')
        return _app_name
    
    def on_icon(self):
        self.songLabel = Label(
            pos_hint={'center_x': 0.9, 'center_y': 0.05 },
            size_hint=(1, 1),
            font_size=18
        )
        self.add_widget(self.songLabel)


Factory.register('Root', cls=Root)

# Factory.register('FileChooserLayer', cls=FileChooserLayer)

Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('DatePicker', cls=DatePicker)
Factory.register('FuelSupply', cls=FuelSupply)
Factory.register('MainPage', cls=MainPage)


# Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
   
    Editor4().run()
    
    print(
        f"{path_initial} |, \n\
        {registry} |, \n\
        {path_final} |, \n\
        {report} |, \n\
        {date} |, \n\
        {fuel_type} |, \n\
        {supply_form.pickup} |, \n\
        {supply_form.arrival} |, \n\
        {supply_form.residue} | "
        )

    print(dir(Editor4))
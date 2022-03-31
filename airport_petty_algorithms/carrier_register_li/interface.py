import kivy
from kivy.app import App
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
    FuelArrivedField,
    ParseXLSXData
)


from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.widget import Widget
from kivy.core.window import Window

### *** Layouts *** ###

from kivy.uix.image import AsyncImage
from kivy.lang import Builder
from kivy.uix.popup import Popup

### time ###
import time

### encoding ###
import hashlib
import hmac

from kivy.config import Config
Config.set('graphics', 'resizable', True)
kivy.require('2.1.0')

# Designate our .kv desighn file
Builder.load_file('rounded_button.kv')


# class RootWidget(FloatLayout):

#     # signal white
#     rgb = [240.0, 240.0, 240.0, 0.0]

#     def __init__(self, rgb=rgb, **kwargs):
#         self.r = rgb[0]/255.0
#         self.g = rgb[1]/255.0
#         self.b = rgb[2]/255.0
#         self.a = rgb[3]/255.0
#         # make sure we aren't overriding any important functionality
#         super(RootWidget, self).__init__(**kwargs)

#         # let's add a Widget to this layout
#         self.add_widget(
#             Button(
#                 background_color =(self.r, self.g, self.b, 1),
#                 # color of the text
#                 # color = [0, 0, 0],
#                 #border = (30, 30, 30, 30),
#                 text="Window",
#                 size_hint=(.8, .3),
#                 pos_hint={'center_x': .5, 'center_y': .7}))
        
#         self.add_widget(
#             Button(
#                 background_color =(self.r, self.g, self.b, 1),
#                 text="Date",
#                 #border = (5, 5, 5, 5),
#                 size_hint=(.1, .06),
#                 pos_hint={'center_x': .1, 'center_y': .2}),
#                 )
#         widget = RoundedRectangleWidget()
#         widget.prepare()
#         self.add_widget(widget)

WHITE = (255/255, 255/255, 255/255, 1)
SIGNAL_WHITE = (240/255, 240/255, 240/255, 0)
PURE_WHITE = (240/255, 240/255, 240/255, 1)
TRAFFIC_GREY = (83/255, 83/255, 83/255, 1)
MINT_GREEN = (155/255, 255/255, 152/255, 0.8)
# class RoundedRectangleWidget(Widget):
#     def build(self):
#         pass

'''
# Builder.load_string(
# <RectangleWidget>:
#     h: root.height/4
#     # color: (1,0,0,1)

#     canvas:
#         Color: 
#             rgb: (180/255, 180/255, 180/255, 1)
#         Rectangle:
#             size: (200, 75)
# )
'''

## *** Rectnagle Wifget for messages *** ###
class RectangleWidget(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RectangleWidget, self).__init__(**kwargs)

        with self.canvas.before:
            Color(*TRAFFIC_GREY)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=(400, 200), pos=(200, 350))


        self.bind(pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

# print(RectangleWidget().__dict__.get('rect').pos)
# inst = RectangleWidget()
# print(dir(inst))
# print(inst.center)

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


# inst = DialogBox()
# print(dir(inst))
# print(inst.center)

class ConfirmPopup(DialogBox):
    """ ConfirmPopup is for True/False confirmation popup with a message """
    confirm_prompt = StringProperty("")

    def __init__(self, message, action, *args, **kwargs):
        self.title = "Confirm"
        self.confirm_prompt = message
        self.action = action
        super(ConfirmPopup, self).__init__(*args, **kwargs)

    @staticmethod
    def create_and_open(message, action, *args, **kwargs):
        if DialogBox.my_active == None:
            DialogBox.my_active = \
                ConfirmPopup(*args, message=message,
                        action=action, **kwargs)
            DialogBox.my_active.open()

    def ok_confirm(self):
        if super(ConfirmPopup, self).ok_confirm():
            self.action()



class MyTextInput(TextInput):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.text = ""
            return True
        return super(MyTextInput, self).on_touch_down(touch)

kv_string = """
ScreenManager:
    id: manager
    Screen:
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Why does it clear multiple inputs? And why do they get cleared after touch_up?'
            MyTextInput:
                text: 'Write Your Name'
            MyTextInput:
                text: 'Write Your Last Name'  
            MyTextInput:
                text: 'Write Your Phone Number'
"""




class MyFloatLayout(FloatLayout):

    '''
    ===========================================================
    This class represents a 'A First window Layout'
    ===========================================================
    Attrs:
        :param : error message for inappropriate field input
        :type msg: <str>
    
    .. note::
        Creating button-var-add_widget(var)-bind defines <kivy.uix.button.Button object>
        & further using this object for retrieving necessary data
    '''

    # signal white
    rgb = SIGNAL_WHITE

    # button
    rgb_btn = PURE_WHITE

    rgb_submit = MINT_GREEN

    def __init__(self, **kwargs):
        # call grid_layout contructor
        super(MyFloatLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 2
    
        # add widget name of the app pos=(200, 350)
        self.message = self.add_widget(
            Label(
                color=TRAFFIC_GREY,
                pos=(0, 200)
                )
            )
        

        # grey box for messages
        # self.field = self.add_widget(RectangleWidget())
        
        # input box for messages
        # add input box
        # self.add_widget(
        #     TextInput(
        #         multiline=False,
        #         size_hint=(.8, .3),
        #         pos_hint={'center_x': .5, 'center_y': .7}
        #         )
        #     )
        self.date_input = TextInput(
            multiline=False,
            size_hint=(.2, .07),
            pos_hint={'center_x': .20, 'center_y': .7},
            # on_release=self.process_date
        )

        self.arrival_input = TextInput(
            multiline=False,
            size_hint=(.2, .07),
            pos_hint={'center_x': .30, 'center_y': .9},
            # on_release=self.process_fuel_arrival

        )
        
        ### *** button with ready made VALUE *** ###
        self.type1 = Button(
                background_color=self.rgb_btn,
                text="RT",
                border = (6, 6, 6, 6),
                size_hint=(.1, .05),
                pos_hint={'center_x': .15, 'center_y': .2},
                # on_press=self.select_fuel,
                # on_release=self.clear_inputs
            )

        self.add_widget(self.type1)
        self.type1.bind(on_press=self.select_fuel)

        self.type2 = Button(
                background_color=self.rgb_btn,
                text="Jet A-1",
                border = (6, 6, 6, 6),
                size_hint=(.1, .05),
                pos_hint={'center_x': .15, 'center_y': .28},
                # on_press=self.select_fuel,
                # on_release=self.clear_inputs
            )

        self.add_widget(self.type2)
        self.type2.bind(on_press=self.select_fuel)

        self.process = Button(                
            background_color=self.rgb_submit,
            text="Submit",
            border = (6, 6, 6, 6),
            size_hint=(.1, .05),
            pos_hint={'center_x': .15, 'center_y': .12},
            # on_release = self.process_application
        )

        ##########################################################

        ### *** textinput date with input VALUE *** ###
        # self.date = TextInput(
        #         multiline=False,
        #         size_hint=(.2, .07),
        #         pos_hint={'center_x': .20, 'center_y': .7}
        #     )
        # self.add_widget(self.date)

        # self.submit = Button(
        #         text="Submit",
        #         font_size="20sp",
        #         size_hint=(.1, .05),
        #         pos_hint={'center_x': .15, 'center_y': .15},
        #     )
        # self.add_widget(self.submit)
        
        # # bind the text input
        # self.submit.bind(on_press=self.select_date)
       ##########################################################

    ### *** FUEL_TYPE *** ###
    def select_fuel(self, instance):
        # close_dialog = Button(                
        #     background_color=self.rgb_btn,
        #     text="Close",
        #     border = (6, 6, 6, 6),
        #     size_hint=(.1, .05),
        #     pos_hint={'center_x': .9, 'center_y': .2}
        # )
        ## instance.text - varibale for ApplicationCore method for FuelTypeSelectField()
        ##  create it without init in order not to process it a couple of times FuelTypeSelectField(TYPE) --> 
        ## : ParseXlsxFile(x)
        ## : submain()
        # self.message = self.add_widget(
        #     Label(
        #         text=f"U have selected the next type fuel type: {instance.text}",
        #         color=TRAFFIC_GREY,
        #         pos=(0, 200)
        #         )
        #     )


        self.add_widget(self.process)
        ## self.process.bind(on_press=self.process_application) ## works change
        self.process.bind(on_press=self.select_date)
        ##################
        self.fuel_type = instance.text ## ----> convert to object
        ##################
        self.message = f"U have selected the next type fuel type: {self.fuel_type}"
        
        dialog = DialogBox(
            title=u'\u274C',
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=False,
            )
       
        # self.add_widget(close_dialog)
        # close_dialog.bind(on_press=dialog.dismiss) #### bind this button
        # close_dialog.bind(on_press=self.process_application) #### bind this button
        # self.process_application()
        
        dialog.open()
        

    ### *** DATE *** ###
    def select_date(self, instance=None):
        try:
            print(self.date_input)
            self.add_widget(self.date_input)
            # bind the date input
            self.process.bind(on_press=self.process_date)
        except Exception as err:
            print(err)

    def process_date(self, instance=None):
        date = self.date_input.text
        print(date) ### +++
        self.process.bind(on_press=self.get_fuel_arrival)
        ##################
        self.date = date ## ----> convert to object
        ##################
        self.message = f"U have selected the next date: {date}"
        self.dialog = DialogBox(
            title=u'\u274C',
            title_size="25sp",
            content=Label(text=self.message),
            pos=(200.0, 350.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=False,
            )
        self.date_input.text = ''
        self.dialog.open()
        


    ## *** FUEL SUPPLY *** ###
    def get_fuel_arrival(self, instance=None):
        try:
            self.add_widget(self.arrival_input)
            # bind the date input
            self.process.bind(on_press=self.process_fuel_arrival)
        except Exception as err:
            print(err)

    def process_fuel_arrival(self, instance=None):
        
        fuel_arrival = self.arrival_input.text
        # print(fuel_arrival) ### +++
        self.process.bind(on_press=self.something_else)
        ################## **** validation **** ########################
        # self.fuel_arrival = fuel_arrival ## ----> convert to object
        ### <class 'parse_data.FuelArrivedField'>
        global fuel
        fuel = FuelArrivedField(fuel_arrival)
        print(type(fuel))
        fuel_arrival = fuel.fuel_arrived
    
        self.message = f"Fuel supply is: {fuel_arrival}"
        if fuel_arrival is None:
            self.message = fuel.error
        ################################################################
        self.dialog = DialogBox(
            title=u'\u274C',
            title_size="25sp",
            content=Label(text=self.message),
            pos=(150.0, 400.0),
            size_hint=(0.5, 0.25),
            size=(400, 200),
            auto_dismiss=False,
            )

        self.dialog.open()
        return fuel_arrival

    def something_else(self, instance):
        self.dialog.dismiss()
        fuel_arrival = self.process_fuel_arrival()
        print(fuel_arrival)
        print(instance)

        # self.message = self.add_widget(
        #     Label(
        #         text=f"U have selected the next date: {date}",
        #         color=TRAFFIC_GREY,
        #         pos=(0, 250)
        #         )
        #     )
        # print(self.message)
        # self.date.text = ''


    def clear_inputs(self, instance):
        self.message = self.add_widget(
            Label(
                text=f"",
                color=TRAFFIC_GREY,
                pos=(0, 200)
                )
            )
    
    def process_application(self, instance):
        ### put all widgets here/
        print(self.fuel_type)
        data = ParseXLSXData(select_fuel=self.fuel_type)
        # data.date = '22-08-2021'
        print(data.__dict__)
    


# print(MyFloatLayout().__dict__)
# inst = RectangleWidget()
# print(dir(inst))
# print(inst.size))        


class ParseDataInterfaceApp(App):
    '''
        ===========================================================
        This class represents a 'A Main App Window'
        ===========================================================
        Attrs:
            :param rgb: error message for inappropriate field input
            :type msg: <str>
        
        .. note::
            get_classname() - aims to get cuurent classname when 
            exceptions raised. Inherited by other field classes.

            Standard App window size: (800px, 600px)

    '''
    # basalt grey colour
    # rgb = [94.1, 94.1, 94.1]

    # signal white
    rgb = [240.0, 240.0, 240.0]

    #app_name = 'Carrier Register'
    app_name = 'Carrier Register'

    
    def build(self):
        Window.clearcolor = SIGNAL_WHITE
        return MyFloatLayout()

    def get_application_name(self):
        _app_name = self.app_name
        _app_name.encode(encoding = 'UTF-8', errors = 'strict')
        return _app_name

if __name__ == '__main__':
    ParseDataInterfaceApp().run()
    
    # print(f"This is fuel {fuel}") # fuel object is in global scope
    

# x = ParseDataInterfaceApp()
# print(dir(x))
# print(x.size)
# print(x.__dict__)
# print(x.get_application_name())

# x = FuelArrivedField()
# button = Button()
# print(dir(button))
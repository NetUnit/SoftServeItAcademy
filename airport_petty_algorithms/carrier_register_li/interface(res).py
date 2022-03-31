from kivy.app import App
from kivy.uix.button import (
    Button,
)

from kivy.uix.label import (
    Label,
)

from kivy.uix.input import (
    TextInput
)

from kivy.graphics import (
    Color,
    Rectangle, 
    RoundedRectangle,
    Ellipse
)

from kivy.uix.gridlayout import (
    Gridlayout
)

from kivy.uix.widget import Widget

from kivy.core.window import Window

### *** Layouts *** ###
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import AsyncImage
from kivy.lang import Builder

from kivy.config import Config
Config.set('graphics', 'resizable', True)

# Designate our .kv desighn file
Builder.load_file('rounded_button.kv')

TEXTURE = 'kiwi.jpg'
YELLOW = (1, .7, 0)
ORANGE = (1, .45, 0)
RED = (1, 0, 0)
WHITE = (1, 1, 1)

class RootWidget(FloatLayout):

    # signal white
    rgb = [240.0, 240.0, 240.0, 0.0]

    def __init__(self, rgb=rgb, **kwargs):
        self.r = rgb[0]/255.0
        self.g = rgb[1]/255.0
        self.b = rgb[2]/255.0
        self.a = rgb[3]/255.0
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # let's add a Widget to this layout
        self.add_widget(
            Button(
                background_color =(self.r, self.g, self.b, 1),
                # color of the text
                # color = [0, 0, 0],
                #border = (30, 30, 30, 30),
                text="Window",
                size_hint=(.8, .3),
                pos_hint={'center_x': .5, 'center_y': .7}))
        
        self.add_widget(
            Button(
                background_color =(self.r, self.g, self.b, 1),
                text="Date",
                #border = (5, 5, 5, 5),
                size_hint=(.1, .06),
                pos_hint={'center_x': .1, 'center_y': .2}),
                )
        widget = RoundedRectangleWidget()
        widget.prepare()
        self.add_widget(widget)

class RoundedRectangleWidget(Widget):
    def prepare(self):
        with self.canvas:
            # Possible radius arguments:
            # 1) Same value for each corner
            Color(*ORANGE)

            # With same radius 20x20
            Button(pos=(50, 275))


class ParseDataInterfaceApp(App):
    
    # basalt grey colour
    # rgb = [94.1, 94.1, 94.1]

    # signal white
    rgb = [240.0, 240.0, 240.0]

    app_name = 'Carrier Register'
    _app_name = 'Carrier Register'
    # def __str__(self):
    #     return
    
    # def __repr__(self):
    #     return

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        
        # Window.clearcolor = (1, 1, 1, 1)
        # return  RootWidget()
        
        with root.canvas.before:
            r = self.rgb[0]
            g = self.rgb[1]
            b = self.rgb[2]
            # Color(r/255.0, g/255.0, b/255.0, 1) 
            self.rect = Rectangle(size=root.size, pos=root.pos, radius=[120])
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    # def build(self):
    #     return Label(text=self.app_name)

    def select_date(self):
        pass


if __name__ == '__main__':
    ParseDataInterfaceApp().run()

# ParseDataInterfaceApp().run()

    x = Button()
    print(x.__dict__)


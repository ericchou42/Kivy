from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class Root(Widget):
    pass

class ALabel(Label):
    def __init__(self, **kwargs):
        super().__init__()
        self.color = "black"
        with self.canvas:
            Color(0, .5, .5, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.updateRect, size=self.updateRect)

    def updateRect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.font_size = 32
            self.color = "red"
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.font_size = 16
            self.color = "black"
            self.outline_color = "olive"

        return super().on_touch_up(touch)

class AButton(Button):

    def __init__(self, **kwargs):
        super().__init__()
        self.color = "blue"
        self.background_color = (1, 1, 0, 1)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = (.5, .5, 0, .5)
            self.opacity = .3
            self.color = "red"

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.background_color = (1, 1, 0, 1)
            self.opacity = 1
            self.color = "blue"

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            print(f"position: {touch}")

class MyApp(App):
    def build(self):
        return Root()

if __name__ == '__main__':
    MyApp().run()
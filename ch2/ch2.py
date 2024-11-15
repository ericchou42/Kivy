from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyLayout(Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)

    def clickBtn(self):
        print(f"Name: {self.name.text}\nAge: {self.age.text}")
        self.name.text= ""
        self.age.text= ""

    def inputName(self):
        print("Input name......")

    def inputAge(self):
        print("Input age......")

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
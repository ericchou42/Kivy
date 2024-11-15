from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 計數初始值
        self.count = 10
        # 總共列
        self.cols = 1

        self.topFrame = GridLayout()
        # 欄位列數
        self.topFrame.cols = 6
        self.lb1 = Label(text="Label 1")
        self.lb2 = Label(text="Label 2")
        self.lb3 = Label(text="Label 3")
        self.lb4 = Label(text="Label 4")
        self.lb5 = Label(text="Label 5")
        self.lb6 = Label(text=f"{self.count}")
        self.topFrame.add_widget(self.lb1)
        self.topFrame.add_widget(self.lb2)
        self.topFrame.add_widget(self.lb3)
        self.topFrame.add_widget(self.lb4)
        self.topFrame.add_widget(self.lb5)
        self.topFrame.add_widget(self.lb6)

        self.add_widget(self.topFrame)
        self.bt = Button(text="Click")
        self.bt.bind(on_press=self.pressed)
        self.add_widget(self.bt)

    def pressed(self, instance):
        self.count += 1
        print(self.count, instance.text)
        self.lb6.text = f"{self.count}"

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivy.core.text import LabelBase
# 註冊自訂字型
LabelBase.register(name="NotoSansTC", fn_regular="NotoSansTC-Regular.ttf")

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # 使用指定的繁體中文字型
        label = Label(text="你好，這是繁體中文", font_name="NotoSansTC", font_size=40)
        
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    MyApp().run()
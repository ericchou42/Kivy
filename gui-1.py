import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import mysql.connector

kivy.require('2.3.0')

# 连接 MySQL 数据库
def insert_data(name, age):
    try:
        connection = mysql.connector.connect(
            host="localhost",  # 数据库地址
            user="root",       # 数据库用户名
            password="",       # 数据库密码
            database="my_database"  # 数据库名称
        )

        cursor = connection.cursor()
        cursor.execute("INSERT INTO test_data (name, age) VALUES (%s, %s)", (name, age))
        connection.commit()
        cursor.close()
        connection.close()

        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Kivy GUI 界面
class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 输入框: 姓名
        self.name_input = TextInput(hint_text="Enter Name", size_hint_y=None, height=40)
        self.layout.add_widget(self.name_input)

        # 输入框: 年龄
        self.age_input = TextInput(hint_text="Enter Age", size_hint_y=None, height=40, input_filter='int')
        self.layout.add_widget(self.age_input)

        # 提交按钮
        submit_button = Button(text="Submit", size_hint_y=None, height=50)
        submit_button.bind(on_press=self.submit_data)
        self.layout.add_widget(submit_button)

        # 结果标签
        self.result_label = Label(text="", size_hint_y=None, height=40)
        self.layout.add_widget(self.result_label)

        return self.layout

    # 提交数据
    def submit_data(self, instance):
        name = self.name_input.text
        age = self.age_input.text

        if name and age:
            # 插入数据到数据库
            success = insert_data(name, age)

            if success:
                self.result_label.text = "Data inserted successfully!"
                self.name_input.text = ""
                self.age_input.text = ""
            else:
                self.result_label.text = "Failed to insert data."
        else:
            self.result_label.text = "Please fill in both fields."

# 运行 Kivy 应用
if __name__ == '__main__':
    MyApp().run()
import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
import serial  # 新增串口模組
import sys
import os
from kivy.uix.spinner import Spinner  # 新增 Spinner 引入
import serial.tools.list_ports  # 新增串口列表工具

# 判斷程式是否在打包後的 .exe 中運行
if getattr(sys, 'frozen', False):
    font_path = os.path.join(sys._MEIPASS, 'NotoSansTC-Regular.ttf')
else:
    font_path = os.path.join(os.path.dirname(__file__), 'NotoSansTC-Regular.ttf')

# 註冊繁體中文字型
LabelBase.register(name="NotoSansTC", fn_regular=font_path)

class DatabaseConnectionApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 初始化 MySQL 連線相關的變數
        self.connection = None
        self.cursor = None
        self.order_number = None
        
        # 初始化串口連線相關的變數
        self.serial_port = None  # 修改為 None，等待用戶選擇
        self.baudrate = 9600
        self.timeout = 1
        self.ser = None
        self.available_ports = []  # 新增可用串口列表
    
    def get_available_ports(self):
        """獲取所有可用的串口列表"""
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return ports if ports else ['無可用串口']

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 新增串口選擇下拉選單
        self.available_ports = self.get_available_ports()
        self.port_spinner = Spinner(
            text='選擇串口',
            values=self.available_ports,
            size_hint_y=5,
            height=40,
            font_name="NotoSansTC",
            font_size=50
        )
        self.port_spinner.bind(text=self.on_port_select)
        layout.add_widget(self.port_spinner)

        # 工單號輸入框
        self.order_number_input = TextInput(
            hint_text='請輸入工單號', 
            size_hint_y=7, 
            height=40, 
            multiline=False, 
            font_name="NotoSansTC",
            font_size=50
        )
        self.order_number_input.bind(on_text_validate=self.query_record)
        layout.add_widget(self.order_number_input)

        # 查詢按鈕
        self.query_button = Button(
            text="查詢", 
            size_hint_y=5, 
            height=40, 
            font_name="NotoSansTC",
            font_size=50
        )
        self.query_button.bind(on_press=self.query_record)
        layout.add_widget(self.query_button)

        # 顯示查詢結果的標籤
        self.result_label = Label(
            text="查詢結果會顯示在這裡", 
            size_hint_y=None, 
            height=100, 
            font_name="NotoSansTC",
            font_size=50
        )
        layout.add_widget(self.result_label)

        # 重量顯示標籤
        self.weight_label = Label(  # 新增重量顯示標籤
            text="目前重量: 等待讀取...", 
            size_hint_y=None, 
            height=100, 
            font_name="NotoSansTC",
            font_size=50
        )
        layout.add_widget(self.weight_label)

        # 按鈕區域
        self.button_box = BoxLayout(size_hint_y=20, height=60, spacing=20)
        layout.add_widget(self.button_box)

        # 連接資料庫
        self.connect_to_database()
        
        # 連接串口
        # self.connect_to_serial()  # 移除這行，等待用戶選擇串口後再連接

        return layout
    
    def connect_to_serial(self):
        """連接到串口"""
        try:
            self.ser = serial.Serial(self.serial_port, self.baudrate, timeout=self.timeout)
            print(f"已連接到串口 {self.serial_port}")
        except serial.SerialException as e:
            print(f"串口連接錯誤: {e}")
            self.weight_label.text = "無法連接到電子秤，請檢查連接！"

    def read_weight(self):
        """從串口讀取重量數據"""
        try:
            if self.ser and self.ser.in_waiting > 0:
                data = self.ser.readline().decode('utf-8').strip()
                print(f"收到重量數據: {data}")
                self.weight_label.text = f"目前重量: {data}公斤"
                return data
            return None
        except serial.SerialException as e:
            print(f"讀取重量錯誤: {e}")
            self.weight_label.text = "讀取重量失敗"
            return None

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="my_database",
                port=3306
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("成功連接到資料庫")
        except mysql.connector.Error as err:
            print(f"資料庫連接錯誤: {err}")
            self.result_label.text = "無法連接資料庫，請檢查設定！"

    def query_record(self, instance):
        if not self.cursor:
            self.result_label.text = "資料庫連接失敗，無法查詢。"
            return

        self.order_number = self.order_number_input.text.strip()
        
        if self.order_number:
            self.cursor.execute("SELECT 工單號, 名稱, 是否合格 FROM test_data WHERE 工單號 = %s", (self.order_number,))
            result = self.cursor.fetchone()

            if result:
                名稱 = result["名稱"]
                是否合格 = "合格" if result["是否合格"] else "不合格"
                self.result_label.text = f"名稱: {名稱} 是否合格: {是否合格}"
                
                self.button_box.clear_widgets()
                btn_qualified = Button(text="合格", font_name="NotoSansTC", font_size=50)
                btn_qualified.bind(on_press=self.mark_qualified)
                self.button_box.add_widget(btn_qualified)
                
                btn_not_qualified = Button(text="不合格", font_name="NotoSansTC", font_size=50)
                btn_not_qualified.bind(on_press=self.mark_not_qualified)
                self.button_box.add_widget(btn_not_qualified)
            else:
                self.result_label.text = "找不到該工單號的資料"
                self.button_box.clear_widgets()
        else:
            self.result_label.text = "請輸入有效的工單號"
            self.button_box.clear_widgets()

    def mark_qualified(self, instance):
        """將工單號標記為合格並更新重量"""
        weight = self.read_weight()
        if weight:
            self.update_record(True, weight)
        else:
            self.result_label.text = "無法讀取重量，請確認電子秤連接"

    def mark_not_qualified(self, instance):
        """將工單號標記為不合格並更新重量"""
        weight = self.read_weight()
        if weight:
            self.update_record(False, weight)
        else:
            self.result_label.text = "無法讀取重量，請確認電子秤連接"

    def update_record(self, is_qualified, weight):
        """更新資料庫記錄"""
        if self.cursor and self.order_number:
            try:
                self.cursor.execute("""
                    UPDATE test_data 
                    SET 是否合格 = %s, 重量 = %s 
                    WHERE 工單號 = %s
                """, (is_qualified, weight, self.order_number))
                self.connection.commit()
                self.result_label.text = f"工單號 {self.order_number} 更新為 {'合格' if is_qualified else '不合格'}，重量: {weight}公斤"
                print(f"已更新工單號 {self.order_number} 為 {'合格' if is_qualified else '不合格'}，重量: {weight}公斤")
            except mysql.connector.Error as err:
                self.result_label.text = f"更新錯誤: {err}"

    def on_stop(self):
        """結束時關閉所有連接"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("資料庫連線已關閉")
            
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"串口 {self.serial_port} 已關閉")

    def on_port_select(self, spinner, text):
        """當用戶選擇串口時觸��"""
        if text != '無可用串口':
            self.serial_port = text
            self.connect_to_serial()

if __name__ == '__main__':
    DatabaseConnectionApp().run()
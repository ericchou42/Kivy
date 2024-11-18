import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase  # 匯入 LabelBase 用於字型註冊

# 註冊繁體中文字型
LabelBase.register(name="NotoSansTC", fn_regular="NotoSansTC-Regular.ttf")

class DatabaseConnectionApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 初始化 MySQL 連線相關的變數
        self.connection = None
        self.cursor = None
        self.order_number = None  # 儲存查詢的工單號
    
    def build(self):
        # 設定主界面的 BoxLayout 排列方式為垂直
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 工單號輸入框，提示文字為"請輸入工單號"
        self.order_number_input = TextInput(hint_text='請輸入工單號', size_hint_y=5, height=40, multiline=False, font_name="NotoSansTC")
        layout.add_widget(self.order_number_input)

        # 查詢按鈕，綁定查詢事件
        self.query_button = Button(text="查詢", size_hint_y=5, height=40, font_name="NotoSansTC",font_size=50)
        self.query_button.bind(on_press=self.query_record)
        layout.add_widget(self.query_button)

        # 顯示查詢結果的標籤
        self.result_label = Label(text="查詢結果會顯示在這裡", size_hint_y=None, height=100, font_name="NotoSansTC",font_size=50)
        layout.add_widget(self.result_label)

        # 按鈕區域，用於放置查詢後的「合格」和「不合格」按鈕
        self.button_box = BoxLayout(size_hint_y=20, height=60, spacing=20)
        layout.add_widget(self.button_box)

        # 連接資料庫
        self.connect_to_database()

        return layout

    def connect_to_database(self):
        """ 連接到 MySQL 資料庫 """
        try:
            # 使用 MySQL Connector 進行連接
            self.connection = mysql.connector.connect(
                host="localhost",  # MySQL 伺服器主機
                user="root",       # 使用者名稱
                password="",       # 密碼
                database="my_database",  # 資料庫名稱
                port=3306          # 端口號
            )
            # 使用 dictionary=True 將結果以字典格式返回
            self.cursor = self.connection.cursor(dictionary=True)
            print("成功連接到資料庫")
        except mysql.connector.Error as err:
            print(f"資料庫連接錯誤: {err}")

    def query_record(self, instance):
        """ 查詢工單號並顯示資料 """
        # 取得工單號輸入值並去除空格
        self.order_number = self.order_number_input.text.strip()
        
        if self.order_number:
            # 執行 SQL 查詢，查找指定工單號的資料
            self.cursor.execute("SELECT 工單號, 名稱, 是否合格 FROM test_data WHERE 工單號 = %s", (self.order_number,))
            result = self.cursor.fetchone()

            if result:
                # 顯示查詢到的名稱和合格狀態
                名稱 = result["名稱"]
                是否合格 = "合格" if result["是否合格"] else "不合格"
                self.result_label.text = f"名稱: {名稱}\n是否合格: {是否合格}"
                
                # 動態生成合格和不合格按鈕
                self.button_box.clear_widgets()  # 清除先前的按鈕
                btn_qualified = Button(text="合格", font_name="NotoSansTC",font_size=50)
                btn_qualified.bind(on_press=self.mark_qualified)
                self.button_box.add_widget(btn_qualified)
                
                btn_not_qualified = Button(text="不合格", font_name="NotoSansTC",font_size=50)
                btn_not_qualified.bind(on_press=self.mark_not_qualified)
                self.button_box.add_widget(btn_not_qualified)
            else:
                # 若無結果，顯示找不到資料訊息
                self.result_label.text = "找不到該工單號的資料"
                self.button_box.clear_widgets()  # 清除按鈕
        else:
            # 若輸入無效，顯示錯誤訊息
            self.result_label.text = "請輸入有效的工單號"
            self.button_box.clear_widgets()  # 清除按鈕

    def mark_qualified(self, instance):
        """ 將工單號的是否合格標記為合格 """
        self.update_record(True)

    def mark_not_qualified(self, instance):
        """ 將工單號的是否合格標記為不合格 """
        self.update_record(False)

    def update_record(self, is_qualified):
        """ 更新 '是否合格' 欄位 """
        if self.cursor and self.order_number:
            try:
                # 執行 SQL 更新語句
                self.cursor.execute("""
                    UPDATE test_data 
                    SET 是否合格 = %s 
                    WHERE 工單號 = %s
                """, (is_qualified, self.order_number))
                # 提交更新
                self.connection.commit()
                # 更新後刷新顯示的狀態
                self.result_label.text = f"工單號 {self.order_number} 更新為 {'合格' if is_qualified else '不合格'}"
                print(f"已更新工單號 {self.order_number} 為 {'合格' if is_qualified else '不合格'}")
            except mysql.connector.Error as err:
                self.result_label.text = f"更新錯誤: {err}"

    def on_stop(self):
        """ 結束時關閉資料庫連線 """
        # 若連線仍開啟，則關閉連線
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("資料庫連線已關閉")

if __name__ == '__main__':
    # 啟動應用程式
    DatabaseConnectionApp().run()

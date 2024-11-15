import mysql.connector

# 連接到 MySQL 資料庫
try:
    connection = mysql.connector.connect(
        host="localhost",  # MySQL 伺服器地址（可以使用 "127.0.0.1" 或 "localhost"）
        user="root",       # MySQL 用戶名
        password="",       # MySQL 密碼（如果有的話）
        database="my_database",  # 使用的資料庫名稱
        port=3306          # MySQL 預設端口
    )

    # 檢查是否成功連接
    if connection.is_connected():
        print("成功連接到 MySQL 資料庫")

        # 獲取資料庫伺服器資訊
        db_info = connection.get_server_info()
        print(f"資料庫伺服器版本: {db_info}")

except mysql.connector.Error as err:
    print(f"連接失敗: {err}")
    
finally:
    if connection.is_connected():
        connection.close()
        print("資料庫連線已關閉")
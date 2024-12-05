from zebra import Zebra

# 創建 Zebra 對象，並指定打印機隊列名稱（如 'ZDesigner ZT610-600dpi ZPL'）
zebra_printer = Zebra('ZDesigner ZT610-600dpi ZPL')


# 定義條碼位置變數
x_position = 300  # 條碼的X軸起始位置(點)
y_position = 300  # 條碼的Y軸起始位置(點)

# 定義文字區域變數
text_width = 800  # 文字區域寬度(點)
text_lines = 1    # 文字行數
text_spacing = 0  # 行距
text_align = "C"  # 文字對齊方式: C=置中, L=靠左, R=靠右

# 定義條碼變數
barcode_height = 100  # 條碼高度(點)
barcode_text = "FD321866"  # 條碼內容

# 組合 ZPL 指令 - Code 128 條碼置中
zpl_command = (
    f"^XA"                # 開始 ZPL 指令
    f"^FO{x_position},{y_position}"  # 設定條碼起始位置
    f"^FB{text_width},{text_lines},{text_spacing},{text_align}"  # 設定文字區域格式
    f"^BY2"              # 設定條碼模組寬度為2點
    f"^BCN,{barcode_height},Y,N,N"  # 設定 Code 128 條碼參數: N=正常方向, Y=顯示文字, N=不反白, N=不產生檢查碼
    f"^{barcode_text}" # 設定條碼內容
    f"^FS"              # 結束欄位
    f"^XZ"              # 結束 ZPL 指令
)

# 發送 ZPL 指令到 Zebra 打印機
zebra_printer.output(zpl_command)
print("ZPL 指令已成功發送到打印機。")

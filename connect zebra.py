from zebra import Zebra

# 創建 Zebra 對象，並指定打印機隊列名稱（如 'ZDesigner ZT610-600dpi ZPL'）
zebra_printer = Zebra('ZDesigner ZT610-600dpi ZPL')

# 指定您要發送的 ZPL 指令
zpl_command = "^XA^FO50,50^ADN,36,20^FDHello, Zebra!^FS^XZ"

# 發送 ZPL 指令到 Zebra 打印機
zebra_printer.output(zpl_command)
print("ZPL 指令已成功發送到打印機。")

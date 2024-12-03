# OptimizationFlow
- **author:`Eric`**

## python pip 路徑注意事項
```
pip安裝路徑
pip show pip
```

# 建立虛擬環境
python3.12 -m venv .venv

# (Windows)
py -m venv .venv

# 啟動 (Linux / macOS)
source .venv/bin/activate

# 啟動 (Windows)
.venv\Scripts\activate.ps1

# 安裝套件
pip install -r requirements.txt

# 開啟服務
fastapi dev main.py

# 離開
deactivate

# Kivy安裝
pip install kivy

# kivy教學
https://www.youtube.com/watch?v=3x9jx29hA68
https://www2.nkust.edu.tw/~shanhuen/PythonTutorialHtml/Kivy.html

# 打包方式
## https://dataxujing.github.io/create_apps_in_kivy/chapter6/
pip install pyinstaller

-F [全部打包]
--onefile[單一執行檔]
--icon=your_icon.ico[執行檔圖示]
--name=your_app_name[執行檔名稱]
-F：生成一个文件夹，里面是多文件模式，启动快。
-D：仅仅生成一个文件，不暴露其他信息，启动较慢。
-w：窗口模式打包，不显示控制台。
--name name.exe name.py [命名]

## 最終指令
pyinstaller -F -w --add-data "NotoSansTC-Regular.ttf;." main.py

## .sepc set
```
from kivy_deps import sdl2, glew
```
```coll = COLLECT(
a.zipfiles,
*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
)
```
## Zebra 控制規則
https://support.zebra.com/cpws/docs/zpl/zpl_Exercises.pdf


# commit 規範
```
Message Header: <type>(<scope>): <subject>
```
*   type（必要）：commit 的類別，如：feat(建立), fix(修改), docs, style, refactor, test, chore
*   scope（可選）：commit 影響的範圍，如：資料庫、控制層、模板層等，視專案不同改變
*   subject（必要）：commit 的簡短描述，不超過 50 個字元，結尾不加句號



ZPL 中列印條碼的規則與方法：

### 1. 一維條碼 (1D Barcode)

#### Code 128 條碼
```zpl
^XA
^FO50,50          # 起始位置
^BY2              # 設定條碼寬度（1-10）
^BCN,100,Y,N,N    # 條碼設定
^FD123456789^FS   # 條碼內容
^XZ
```

**^BC 參數說明：**
- N: 正常方向
- 100: 條碼高度
- Y: 顯示人眼可讀文字
- N: 不反白
- N: 不產生 check digit

#### Code 39 條碼
```zpl
^XA
^FO50,50
^BY2
^B3N,100,Y,N,N    # Code 39 條碼
^FD123ABC^FS
^XZ
```

#### EAN-13 條碼
```zpl
^XA
^FO50,50
^BY2
^BEN,100,Y,N      # EAN-13 條碼
^FD123456789012^FS
^XZ
```

### 2. 二維條碼 (2D Barcode)

#### QR Code
```zpl
^XA
^FO50,50
^BQN,2,10         # QR Code 設定
^FDMM,AAhttps://example.com^FS
^XZ
```

**^BQ 參數說明：**
- N: 正常方向
- 2: QR Code 模型（1或2）
- 10: 放大倍數（1-10）

#### Data Matrix
```zpl
^XA
^FO50,50
^BXN,5,200        # Data Matrix 設定
^FDYour Data Here^FS
^XZ
```

### 3. 常用條碼類型指令

| 指令 | 條碼類型 |
|------|----------|
| ^BC  | Code 128 |
| ^B3  | Code 39  |
| ^BE  | EAN-13   |
| ^B2  | Code 2 of 5 Interleaved |
| ^BQ  | QR Code  |
| ^BX  | Data Matrix |
| ^BR  | RSS-14   |

### 4. 條碼參數設定

#### 條碼寬度設定 (^BY)
```zpl
^BY w,r,h
```
- w: 窄條寬度（1-10 點）
- r: 寬條與窄條比例（2.0-3.0）
- h: 條碼高度（以點為單位）

### 5. 實用範例

#### 帶有標題的 Code 128 條碼
```zpl
^XA
^FO50,20
^ADN,30,20        # 標題文字設定
^FDProduct Code:^FS
^FO50,60
^BY3
^BCN,100,Y,N,N
^FD123456789^FS
^XZ
```

#### 多個條碼組合
```zpl
^XA
# 一維條碼
^FO50,50
^BY2
^BCN,80,Y,N,N
^FD123456^FS

# QR Code
^FO50,200
^BQN,2,8
^FDMM,AAhttps://example.com^FS
^XZ
```

### 6. 注意事項

1. **資料格式**
   - 確保資料符合所選條碼類型的規範
   - 某些條碼類型有固定長度要求（如 EAN-13 需要 12-13 位）

2. **列印品質**
   - 使用 ^BY 調整條碼寬度以確保可讀性
   - 考慮列印解析度選擇適當的條碼大小

3. **位置放置**
   - 確保條碼不會超出標籤邊界
   - 預留足夠的空白邊距

4. **人眼可讀文字**
   - 建議在重要場合開啟人眼可讀文字
   - 可以通過調整參數控制文字大小和位置

這些是基本的條碼列印規則，您可以根據實際需求調整參數來獲得最佳的列印效果。如果需要更專業的條碼設定，建議參考 Zebra 的官方技術文件。
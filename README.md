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


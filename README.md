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



## Zebra 控制規則
https://support.zebra.com/cpws/docs/zpl/zpl_Exercises.pdf


# commit 規範
```
Message Header: <type>(<scope>): <subject>
```
*   type（必要）：commit 的類別，如：feat(建立), fix(修改), docs, style, refactor, test, chore
*   scope（可選）：commit 影響的範圍，如：資料庫、控制層、模板層等，視專案不同改變
*   subject（必要）：commit 的簡短描述，不超過 50 個字元，結尾不加句號

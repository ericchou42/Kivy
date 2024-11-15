-- 表單名稱
CREATE TABLE test1_data (
    -- ID
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- UUID
    uuid CHAR(36) NOT NULL,
    -- 日期、時間
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -- 生產單位
    -- 工單號
    -- 品項名稱
    project_name VARCHAR(255) NOT NULL,
    -- 車台
    -- 工序
    -- 改車人員
    -- 顧車人員
    -- 單重
    -- 淨重
    -- 數量(計算)
    quantity INT NOT NULL,
    -- 作業員
    -- 箱數
    
    -- 料號
    -- 檢查人員
    -- 後續單位
    -- 每箱淨重
    -- 備註
    -- HSF
    -- 異常色（紅色）
);




-- MySQL 語法
-- https://note.drx.tw/2012/12/mysql-syntax.html


-- 常用資料庫資料型態
-- 1. INT (整數)
-- 2. CHAR (1~255字元字串)
-- 3. VARCHAR (不超過255字元不定長度字串)
-- 4. TEXT (不定長度字串最多65535字元)
# EIS Data Converter (Batch Processing Tool)

這是一個專為 EIS (電化學阻抗譜) 數據設計的批次轉換工具。
它可以自動掃描 `input` 資料夾中的所有 `.fcd` 檔案，轉換後存入 `output` 資料夾。

## 功能特點

* **自動分流**：自動建立 input/output 資料夾，管理更清楚。
* **批次處理**：一次可以處理成千上萬個檔案。
* **格式轉換**：將 .fcd 轉換為乾淨的 .csv。
* **原始數據**：保留原始阻抗虛部數值 (Z")，不進行變號。

## 使用方法 (Windows/Mac)

1. 下載並執行 `converter` 軟體。
2. 第一次執行時，程式會自動建立一個 `input` 資料夾。
3. 將你的 `.fcd` 檔案全部放入 `input` 資料夾內。
4. 再次執行軟體。
5. 完成後，請至 `output` 資料夾查看結果。

## 開發者資訊
* Language: Python 3.14
* Libraries: pandas, pyinstaller
import pandas as pd
import os
import sys

# --- 1. 鎖定程式所在位置 ---
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(os.path.abspath(__file__))

# 定義輸入和輸出資料夾的路徑
input_folder = os.path.join(application_path, 'input')
output_folder = os.path.join(application_path, 'output')

def process_file(file_path, file_name):
    try:
        # 尋找數據開始行
        header_line = 0
        with open(file_path, 'r', encoding='ISO-8859-1') as f: 
            lines = f.readlines()
            for i, line in enumerate(lines):
                if 'End Comments' in line:
                    header_line = i + 1
                    break
        
        # 讀取數據
        df = pd.read_csv(file_path, 
                         skiprows=header_line, 
                         sep='\t',        
                         header=None, 
                         decimal=',')     

        # 提取欄位 (頻率, 實部, 原始虛部)
        output_df = pd.DataFrame()
        output_df['Frequency (Hz)'] = df[11]
        output_df["Z' (Ohm)"] = df[12]
        output_df['Z" (Ohm)'] = df[13]

        # 設定輸出路徑 (存到 output 資料夾)
        output_filename = os.path.splitext(file_name)[0] + ".csv"
        save_path = os.path.join(output_folder, output_filename)

        output_df.to_csv(save_path, index=False, header=False)
        print(f"✅ 成功：{file_name}")
        return True
        
    except Exception as e:
        print(f"❌ 失敗：{file_name} ({e})")
        return False

def main():
    print(f"程式位置：{application_path}")
    print("------------------------------------------------")

    # 1. 檢查 input 資料夾是否存在
    if not os.path.exists(input_folder):
        print("⚠️  找不到 'input' 資料夾！")
        print(f"--> 我已經幫你在這裡建立了一個：{input_folder}")
        os.makedirs(input_folder)
        print("請把 .fcd 檔案放進去後，再執行一次程式。")
        input("\n按 Enter 鍵結束...")
        return

    # 2. 自動建立 output 資料夾 (如果沒有的話)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"--> 已自動建立輸出資料夾：{output_folder}")

    # 3. 搜尋 input 裡的檔案
    fcd_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.fcd')]
    
    if not fcd_files:
        print(f"⚠️  'input' 資料夾內沒有 .fcd 檔案。")
        print("請放入檔案後再執行。")
    else:
        print(f"📂 發現 {len(fcd_files)} 個檔案，準備輸出到 'output' 資料夾...")
        print("------------------------------------------------")
        
        count = 0
        for file_name in fcd_files:
            full_path = os.path.join(input_folder, file_name)
            if process_file(full_path, file_name):
                count += 1
        
        print("------------------------------------------------")
        print(f"🎉 全部完成！請到 'output' 資料夾查看結果。")

    input("\n按 Enter 鍵結束程式...")

if __name__ == "__main__":
    main()
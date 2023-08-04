import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# 创建tkinter窗口并隐藏
root = tk.Tk()
root.withdraw()

# 弹出文件选择框，让用户选择多个cv Excel文件
cv_files = filedialog.askopenfilenames(title='选择处理文件' , filetypes=[("Excel files", "*.xls;*.xlsx;*.csv;*.txt")])


# 弹出文件选择框，让用户选择背景电流文件
bg_file = filedialog.askopenfilename(title='选择背景电流文件' ,filetypes=[("Excel files", "*.xls;*.xlsx;*.csv")])

# 读取背景电流数据
bg_data = pd.read_csv(bg_file)

# 创建保存结果的文件夹
result_folder = os.path.dirname('D:') + os.sep + '扣除基线电流'

if not os.path.exists(result_folder):
    os.mkdir(result_folder)

# 遍历每个cv文件并进行处理
for cv_file in cv_files:
    # 读取需要处理的数据
    data = pd.read_csv(cv_file)

    # 读取第一列数据
    col1 = data.iloc[:, 0]

    # 读取第二列数据
    col2 = data.iloc[:, 1]
    x = []
    y = []

    # 将第二列数据减去背景电流
    for i in range(len(col1)):
        if col1[i] in bg_data.iloc[:, 0].values  and type(col1[i]) != str:
            j = list(bg_data.iloc[:, 0]).index(col1[i])
            y.append(col2[i] - bg_data.iloc[j, 1])
            x.append(col1[i])

    # 将处理后的数据保存到结果文件夹中
    result_file = os.path.join(result_folder, os.path.basename(cv_file))
    result_file = result_file.replace('csv', 'xlsx')
    pd.DataFrame({'电压': x, '电流': y}).to_excel(result_file, index=False)
    print(f"{cv_file} 处理完成，并保存到 {result_file} 中。")
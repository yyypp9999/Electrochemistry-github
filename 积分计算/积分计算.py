import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
import scipy.integrate

# 创建tkinter窗口并隐藏
root = tk.Tk()
root.withdraw()

# 弹出文件选择框，让用户选择多个LSV Excel文件
lsv_files = filedialog.askopenfilenames(title='选择数据文件 请命名为编号-序号' , filetypes=[("Excel files", "*.xls;*.xlsx;*.txt")])

numberlist = []
lsvfile_total = []
file_counts = 1
m = 0 #区间1
n = 0.1 #区间2

for lsv_file in lsv_files:

    # 读取需要处理的数据

    lsvfile_total = pd.read_csv(lsv_file)
    lsvfile_total = pd.DataFrame(lsvfile_total)
    lsv_data = lsv_data.drop([0])
    lsvfile_total = lsvfile_total.astype (float)

    for i in range(len(lsvfile_total)):
        if float(lsvfile_total.iloc[i,0]) == m:
            a = i
        
        if float(lsvfile_total.iloc[i,0]) == n:
            b = i
        
    x = lsvfile_total.iloc[a:b, 0]
    y = lsvfile_total.iloc[a:b, 1]

    integrals = []  # 用于存储积分
    
    #计算y对于x的积分
    integral = scipy.integrate.trapz(y, x)
    integrals.append(integral)

    #分割文件名与路径
    (filepath,tempfilename) = os.path.split(lsv_file)
    #分割文件名与后缀
    (filename,extension) = os.path.splitext(tempfilename)
    
    number = filename.split("-")[0]
    numberlist.append(number)

integrals = pd.DataFrame(integrals)
integrals.columns = numberlist

# 创建保存结果的文件夹
result_folder = os.path.dirname('E:') + os.sep +  '整合数据'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)
    
# 将处理后的数据保存到结果文件夹中
result_file = result_folder + os.sep + filename +'Q.csv'
integrals.to_csv(result_file, index=False, encoding='utf-8-sig', header=True)

print('计算完成！')
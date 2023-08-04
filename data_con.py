import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np


# 创建tkinter窗口并隐藏
root = tk.Tk()
root.withdraw()

# 弹出文件选择框，让用户选择多个LSV Excel文件
lsv_files = filedialog.askopenfilenames(title='选择数据文件 请命名为编号-序号' , filetypes=[("Excel files", "*.xls;*.xlsx;*.txt")])

lsvfile_total = []
lsvfile_total = pd.DataFrame(lsvfile_total)
file_counts = 1

# 遍历每个cv文件并进行处理
for lsv_file in lsv_files:

    # 读取需要处理的数据
    lsv_data = pd.read_csv(lsv_file)
    sheet = lsv_data
    
    data = lsv_data
    b= np.array(lsv_data)
    li =np.where(b == 'Potential/V')

    li = tuple(map(int, li))
    li = li[0]
    #分割文件名与路径
    (filepath,tempfilename) = os.path.split(lsv_file)
    #分割文件名与后缀
    (filename,extension) = os.path.splitext(tempfilename)

    # 读取第一列数据
    data = data.reset_index(drop=True)
    col1 = data.iloc[li :, 0]
    col2 = data.iloc[li :, 1]
    col1 = col1.reset_index(drop=True)
    col2 = col2.reset_index(drop=True)
    #将col2重命名为文件名
    col1.name = 'Potential/V'
    print(filename)
    number = filename.split("-")[0]
    col1 = col1.to_frame(name="potential/V")
    col2 = col2.to_frame(name=number)
    col1 = col1.reset_index(drop=True)
    col2 = col2.reset_index(drop=True)
    print(col1)
    print(col2)
 
    
    if file_counts == 1:
        lsvfile_total=pd.concat([lsvfile_total,col1],axis=1)
        lsvfile_total=pd.concat([lsvfile_total,col2],axis=1)
        
    else:
        if file_counts > 1:
            lsvfile_total=pd.concat([lsvfile_total,col2],axis=1)

    file_counts += 1        

# 创建保存结果的文件夹
result_folder = os.path.dirname('E:') + os.sep +  '整合数据'
print(lsvfile_total)
# 将处理后的数据保存到结果文件夹中
result_file = result_folder + os.sep + filename +'整合数据.csv'
lsvfile_total = lsvfile_total
lsvfile_total.to_csv(result_file, index=False, encoding='utf-8-sig', header=True)

        




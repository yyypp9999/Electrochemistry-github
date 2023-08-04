import os 
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog

# 创建tkinter窗口并隐藏
root = tk.Tk()
root.withdraw()

i_charge_total = pd.DataFrame()
i_charge = []
numberlist = []
# 弹出文件选择框，让用户选择LSV Excel文件
lsv_file = filedialog.askopenfilename(title='选择数据文件 请命名为编号-序号' , filetypes=[("Excel files", "*.xls; *.xlsx; *.txt; *.csv")])

lsv_data = pd.read_csv(lsv_file)
lsv_data = pd.DataFrame(lsv_data)
lsv_data = lsv_data.drop([0])
lsv_data = lsv_data.astype(float)
lsv_data = lsv_data.reset_index(drop=True)

# 弹出文件选择框，让用户选择多个ECSA Excel文件
ecsa_files = filedialog.askopenfilenames(title='选择数据文件 请命名为编号-序号' , filetypes=[("Excel files", "*.xls;*.xlsx;*.txt; *.csv")])

#逐行读取ecsa文件，并提取Init E (V)，High E (V)，保存到变量
for ecsa_file in ecsa_files:
    ecsa_data = pd.read_csv(ecsa_file)
    sheet = ecsa_data
    data = ecsa_data
    
    #分割文件名与路径
    (filepath,tempfilename) = os.path.split(ecsa_file)
    #分割文件名与后缀
    (filename,extension) = os.path.splitext(tempfilename)
    data.rename = filename
    number = filename.split("-")[2]
    #读表
    for i in range(len(ecsa_data)):
        if  'Init E (V)' in ecsa_data.iloc[i,0]:
            init_e = ecsa_data.iloc[i,0]
            init_e = init_e.split("= ")[1]
            init_e = float(init_e)
            continue
        if 'High E (V)' in ecsa_data.iloc[i,0]:
            high_e = ecsa_data.iloc[i,0]
            high_e = high_e.split("= ")[1]
            high_e = float(high_e)
            continue
        if 'Scan Rate' in ecsa_data.iloc[i,0]:
            scan_rate = ecsa_data.iloc[i,0]
            scan_rate = scan_rate.split("= ")[1]
            scan_rate = float(scan_rate)
            continue
        if 'Segment =' in ecsa_data.iloc[i,0]:
            segment = ecsa_data.iloc[i,0]
            segment = segment.split("= ")[1]
            segment = float(segment)
            continue
        if 'Sample Interval' in ecsa_data.iloc[i,0]:
            sample_interval = ecsa_data.iloc[i,0]
            sample_interval = sample_interval.split("= ")[1]
            sample_interval = float(sample_interval)
            continue
        
    #提取最后一个segment的数据
    m = (high_e - init_e)/sample_interval*2
    m = int(m)
    data = data.reset_index(drop=True)
    data_lasttrace = data.iloc[-m:,:]
    data_lasttrace = data_lasttrace.reset_index(drop=True)

    #提取data_lasttrace中中间电位的数据
    data_halfwave = []
    n = (high_e - init_e)/2 + init_e
    n = round(n,3)
    for i in range(len(data_lasttrace)):
        if float(data_lasttrace.iloc[i,0]) == n:
            k = float(data_lasttrace.iloc[i,1])
            data_halfwave.append(k)

    i_charge_temp = (abs(data_halfwave[0]-data_halfwave[1]))/2
    i_charge.append(i_charge_temp)
    numberlist.append(number)

i_charge = np.array(i_charge).reshape(1,len(i_charge))
i_charge_total = pd.DataFrame(i_charge)
i_charge_total.columns = numberlist

print(i_charge_total)
print(lsv_data)
print(i_charge_total.index)
print(lsv_data.index)

#将LSV中的数据按照列索引除以i_charge中的数据，其中i_charge为一维向量，lsv_data为二维矩阵
J = lsv_data.div(i_charge_total.iloc[0,:],axis=1)
J = J.reindex(columns=numberlist)

print(J)

# 创建保存结果的文件夹
result_folder = os.path.dirname('E:') + os.sep +  '整合数据'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)
    
# 将处理后的数据保存到结果文件夹中
result_file = result_folder + os.sep + filename +'整合数据ECSA.csv'
result_file1 = result_folder + os.sep + filename +'整合数据j.csv'
result_file2 = result_folder + os.sep + filename +'ECSA_lasttrace.csv'
i_charge_total.to_csv(result_file, index=False, encoding='utf-8-sig', header=True)
J.to_csv(result_file1, index=False, encoding='utf-8-sig', header=True)
data_lasttrace.to_csv(result_file2, index=False, encoding='utf-8-sig', header=True)

print('计算完成！')
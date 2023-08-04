import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np


# 创建tkinter窗口并隐藏
root = tk.Tk()
root.withdraw()

# 弹出文件选择框，让用户选择多个LSV Excel文件
lsv_files = filedialog.askopenfilenames(title='重命名功能 请命名为编号-序号' , filetypes=[("Excel files", "*.xls;*.xlsx;*.txt")])

lsvfile_total = []
lsvfile_total = pd.DataFrame(lsvfile_total)
file_counts = 1

def seq():
    num_list_init = np.arange(10,50,5)
    n = 4 #n元
    num_list_init = num_list_init.tolist()
    num_list = num_list_init*n
    def permute(nums):
            from itertools import permutations
            result = []
            for i in permutations(nums,n):
                result.append(list(i))
                
            return result
    y=permute(num_list)
    y=np.array(y)
    sum=np.sum(y, axis=1)
    loc = np.argwhere(sum==90)#SUM为n元比例之和
    loc=loc.tolist()
    n=y[loc, ...] 
    n=np.array(n) 

    new_n = n[ :,0,:]
    a= np.size(new_n,1)

    final=np.array(list(set([tuple(t) for t in new_n])))

    index = np.lexsort((final[:,3],final[:,2],final[:,1],final[:,0],))
    global final_arrange
    final_arrange = final[index]
    return index

index_p = seq()

# 遍历每个cv文件并进行处理
for lsv_file in lsv_files:

    #分割文件名与路径
    (filepath,tempfilename) = os.path.split(lsv_file)
    #在该路径下创建一个新的文件夹
    filepath_rename = filepath + os.sep + '顺序'
    if not os.path.exists(filepath_rename):
        os.mkdir(filepath_rename)
    #分割文件名与后缀
    (filename,extension) = os.path.splitext(tempfilename)
    number_before = filename.split("-")[2]
    temp = int(number_before)-1
    number_after = np.where(index_p == temp)
    number_after = number_after[0][0]+1


    #重命名所有文件并另存到指定文件夹
    newname = str(number_after) + '- Seq' + extension
    newname = filepath_rename + os.sep + newname
    os.rename(lsv_file,newname)
    lsv_file = newname

#将final_arrange保存到csv
m = pd.DataFrame(final_arrange)
m.to_csv(filepath_rename + '\序列.csv')     




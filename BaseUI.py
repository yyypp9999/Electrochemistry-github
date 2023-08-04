import os
import sys
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

class baseUI():
 def __init__(self,master):
    self.root = master
    self.root.config()
    self.root.title('AM系统数据整合')
    width = 800
    height = 600
    g_screenwidth = self.root.winfo_screenwidth()
    g_screenheight = self.root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (g_screenwidth-width)/2, (g_screenheight-height)/2)
    self.root.geometry(alignstr)
    self.initface(self.root)

 def initface(self,master):
    self.master = master
    self.master.config(bg='white')
    self.initface = tk.Frame(self.master,)
    self.initface.grid(row=1,column=0)
    
    #创建文件导入区
    btn = tk.Button(self.initface,text='选择文件',command=self.change, width=12)
    btn.grid(row=1,column=1)
    Datatype = tk.StringVar()
    cvChosen = ttk.Combobox(self.master, width=12, textvariable=Datatype)
    cvChosen['values'] = ('ECSA未处理', 'LSV未处理', 'ECSA处理后', 'LSV处理后')
    cvChosen.grid(row=1,column=1)
    cvChosen.current(0)
    ttk.Label(self.master, text="请将数据文件命名为编号-序号").grid(row=0,column=0)

    #创建文件保存区


 
 def change(self):
    self.initface.destroy()
 
 
 
if __name__ == '__main__':
 root = tk.Tk()
 baseUI(root)
 root.mainloop()






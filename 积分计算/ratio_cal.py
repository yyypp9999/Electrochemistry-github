import os
import sys
import numpy as np

from itertools import combinations
#encoding =utf-8

num_list_init = np.arange(10,50,5)
print(num_list_init)
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
final_arrange = final[index]

'''
MW = np.array([56,55,96,59])  #Fe Mn Mo Co

M_othercompounts = np.inner(final,MW) * 0.01
concentraction = 5 #其他金属浓度单位 mM
v_others = 80 #其它金属溶液总体积 单位ul
m_othercompounts = M_othercompounts * concentraction * v_others 
Pt_m = m_othercompounts * 0.01 #Pt质量分数控制
Pt_v = Pt_m / 195 / 1 #Pt 体积计算 单位mM ul

v_otherssep = np.multiply(final,v_others)   #其他金属体积计算
v_otherssep = np.multiply(v_otherssep,0.01)
'''

v_others = 200 #金属溶液总体积 单位ul
v_otherssep = np.multiply(final,v_others)   #其他金属体积计算
v_otherssep = np.multiply(v_otherssep,0.01)

print('\n')

print(final)

print('\n')
'''
print(Pt_v)
'''
print('\n')

print(v_otherssep)

import pandas as pd
r = pd.DataFrame(final)
r.to_csv('排列乱序版本.csv')
m = pd.DataFrame(final_arrange)
m.to_csv('排列顺序版本.csv')

'''
c = pd.DataFrame(Pt_v)
c.to_csv('1mM Pt体积.csv')
'''
d = pd.DataFrame(v_otherssep)
d.to_csv('四元体积.csv')

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:41:09 2018

@author: 삼성컴퓨터
"""

'''1.수익률 시뮬레이션'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
os.chdir('C:\\Users\삼성컴퓨터\Desktop\python\교수님과제')
data=pd.read_excel('index_data.xlsx', index_col='date')
data=data.fillna(method='ffill')
#1-A번
log=data.resample('W-wed').last().apply(np.log)
ret=log-log.shift(1)
ret_std=ret.std()*np.sqrt(52)
ret_correl=ret.corr(method='pearson')

#%%
#1-B
cov=ret_correl.multiply(ret_std).multiply(ret_std, axis='index')  #위에 std와 correl 안쓰려면 cov함수
simulation=pd.DataFrame(np.random.multivariate_normal(np.zeros(6),cov,100000))
simulation.columns=['SX5Elogret,','HSCEIlogret','HSIlogret','KOSPI2logret','NKYlogret','SPXlogret']
worst_performer=simulation.min(1)
plt.hist(worst_performer, bins=50)
plt.show()
plt.show()
print('mean : ' +str(np.mean(worst_performer)))
print('std  : ' +str(np.std(worst_performer)))
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:43:28 2018

@author: 삼성컴퓨터
"""

'3. 매매손익 계산'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import os 
os.chdir('C:\\Users\삼성컴퓨터\Desktop\python\교수님과제')
#3-1
d=pd.read_csv('trades.csv', header=None,index_col=0)
d.columns=['Index','VOL','Price']
d.index=pd.DatetimeIndex(d.index)
d['VOL']=d.groupby(['Index']).cumsum()  
d['평가금액']=d['VOL']*d['Price']
d.pop('Price')
reslut1=d

#3-2
a=d.groupby(['Index']).resample('BA').last()  
b=d.resample('d').sum().dropna()
b.pop('VOL')
c=b-b.shift(1)
c.columns=['일일손익']
c['누적손익']=c['일일손익'].cumsum()
c['누적손익'].plot()
print('일간 손익분포의 10% 하위 손실금액은', c['일일손익'].quantile(0.1), 
      '그 이하 손실의 조건부 기대값은', c['일일손익'][c['일일손익']<c['일일손익'].quantile(0.1)].mean())
print('일간 손익분포의 5% 하위 손실금액은', c['일일손익'].quantile(0.05), 
      '그 이하 손실의 조건부 기대값은', c['일일손익'][c['일일손익']<c['일일손익'].quantile(0.05)].mean())
print('일간 손익분포의 1% 하위 손실금액은', c['일일손익'].quantile(0.01), 
      '그 이하 손실의 조건부 기대값은', c['일일손익'][c['일일손익']<c['일일손익'].quantile(0.01)].mean())
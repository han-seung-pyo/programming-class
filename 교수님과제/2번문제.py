# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 23:42:00 2018

@author: 삼성컴퓨터
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os
os.chdir('C:\\Users\삼성컴퓨터\Desktop\python\교수님과제')
data=pd.read_excel('index_data.xlsx', index_col='date')
data=data.fillna(method='ffill')
'''2. MDD계산'''
#2-A번
def MDD(data):
    x=np.maximum.accumulate(data)
    y=((x-data)/x).max(axis=0)
    return y
# 2번 B번
df=pd.read_excel('index_data.xlsx',index_col=0).fillna(method='ffill')
res=df.rolling(365).apply(MDD)
res.plot(subplots=True)
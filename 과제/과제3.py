# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:28:54 2018

@author: 삼성컴퓨터
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests, re
import os #directory 변경하는 module
#1-1
response = requests.get("http://www.multivax.com/last_question.html")
story = response.text.split('\r\n<br>\r\n')[1]
story = re.sub("\r|\n|<.*>|--|", '', story)
print(story[:2000])
# Delete special characters
story = re.sub("'s|\'|\"|\.|\,|\?|\:|;|\(|\)|\!", ' ', story)
story = re.sub("\s *", ' ', story)
word_list = story.lower().split(' ')
def word_count(word_list):
    count_array=pd.Series(word_list).value_counts()
    return count_array

word_count(word_list)[:10].plot.bar()
plt.show()

#2-1
os.chdir('C:\\Users\삼성컴퓨터\Desktop\python\중급\pandas exercise 2')  #directory 변경
df = pd.read_excel("vix_data.xlsx").set_index(['DATE']).dropna()

def calc_return(price):
    ret=np.log(price)-np.log(price.shift(1))
    return ret


def calc_delta(price):
    delta=price-price.shift(1)
    return delta

df['SnP500 ret'] = calc_return(df['SnP500'])
df['VIX delta'] = calc_delta(df['VIX'])
df = df.dropna()
df
df.plot.scatter('SnP500 ret', 'VIX delta')
plt.show()
#pd.DataFrame.resample --> time series에 따라서 빈도수 설정하여 다시 frame하는..!

#2-2
def calc_monthly_mean(df):
    df_out=df.resample('1M').mean()
    return df_out

df_out = calc_monthly_mean(df[['SnP500 ret', 'VIX delta']])
df_out.plot.scatter('SnP500 ret', 'VIX delta')
plt.show()

#2-3
def calc_hist_vol(ret, window=20):
    vol_series=ret.rolling(20).std()*np.sqrt(252)
    return vol_series

vol = calc_hist_vol(df['SnP500 ret'])
vol.name = 'SnP500 hist vol'
vix = df['VIX']/100

pd.concat([vol, vix], axis=1).dropna().plot()
plt.show()

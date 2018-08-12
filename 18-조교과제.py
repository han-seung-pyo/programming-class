# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 19:24:40 2018

@author: 삼성컴퓨터
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
#과제 내용 정리 #
'''1.numpy 과제
#점 이어서 길이 구하는 문제.  '''
def length_on_square(n=100000):
    S = np.random.rand(2,10,n)
    S = np.append(S,S[:,0,:].reshape(2,1,n),axis=1)
    length_array = np.sqrt(((S[:,1:,:] - S[:,:-1,:])**2).sum(axis=0)).sum(axis=0)
    return length_array 
    
'''2. pandas 과제. 투자수익 몬테카를로 시뮬레이션'''
def invest_sim(N=100000):
    payoff_array = np.random.randn(N,10).sum(1)
    return payoff_array

def invest_survive(N=100000, T=100):
    ret = np.random.randn(N,T)
    table = ret.cumsum(axis=1) <= -2        #누적 수익이 -2이하 경우 TRUE, 아니면 False
    temp = table*np.arange(1,T+1)           #false에는 곱해도 0, true는 값이 곱해진다. 곱해진 숫자가 폐업 년도
    survival_period_array = np.where(temp==0, T, temp).min(1) # 0이면 T(끝까지 살아남은 기업), 아니면 temp(폐업한 기업)가져오기. 그 중에서 row로 최소값 구한 array
    return survival_period_array

def count_survive(survival_period_array):
    count = (survival_period_array == 100).sum()
    return count

survival_period_array=invest_survive()
print('number of survive 100 years : %d'%(count_survive(survival_period_array)))

'''2-1 블랙숄즈머튼 모델 '''
from scipy.stats import norm
def bsprice(S=100, K=100, r=0.025, q=0.01, sigma=0.25, t=0.24):
    d1 = (np.log(S/K) + (r - q + 0.5*sigma**2)*t)/(sigma*np.sqrt(t))
    d2 = d1 - sigma*np.sqrt(t)
    # Call option price
    C = (S*np.exp(-q*t)*norm.cdf(d1, 0.0, 1.0) 
        - K*np.exp(-r*t)*norm.cdf(d2, 0.0, 1.0))
    # Put option price
    P = (K*np.exp(-r*t)*norm.cdf(-d2, 0.0, 1.0) 
        - S*np.exp(-q*t)*norm.cdf(-d1, 0.0, 1.0))
    price = {'Call':C, 'Put':P}
    return price

'''2-3 수익률 계산''' # 여기에서shif함수 쓰임. shift는 한칸 밑으로 내려서 수익률 계산하기에 편리하게 해줌.
def calc_real_return(df):
    df['real S&P500'] = df['S&P500']*df['CPI'][0]/df['CPI']
    df['return'] = df['S&P500']/df['S&P500'].shift(1) - 1
    return df
df_out = calc_real_return(df)
df_out[['S&P500','real S&P500']].plot()
plt.show()

'''3-1 word counting'''  ##2017년도 기출 문제와 유사
import requests, re    
response = requests.get("http://www.multivax.com/last_question.html")
story = response.text.split('\r\n<br>\r\n')[1]
story = re.sub("\r|\n|<.*>|--|", '', story)
print(story[:2000])
# Delete special characters
story = re.sub("'s|\'|\"|\.|\,|\?|\:|;|\(|\)|\!", ' ', story)   #특수 문자를 제거하는 방법.
story = re.sub("\s *", ' ', story)
word_list = story.lower().split(' ')
def word_count(word_list):
    count_array=pd.Series(word_list).value_counts()
    return count_array
word_count(word_list)[:10].plot.bar()
plt.show()

'''3-2 지수'''
#결측값이란 비어 있는 값. 즉 설묹사에서 대답 안한 것과 같은.
df = pd.read_excel("vix_data.xlsx").set_index(['DATE']).dropna()
def calc_return(price):
    ret=np.log(price)-np.log(price.shift(1))
    return ret

def calc_delta(price):
    delta=price-price.shift(1)
    return delta

df['SnP500 ret'] = calc_return(df['SnP500'])
df['VIX delta'] = calc_delta(df['VIX'])
df=df.dropna()
df
df.plot.scatter('SnP500 ret', 'VIX delta')
plt.show()
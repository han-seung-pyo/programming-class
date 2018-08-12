# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 23:45:40 2018

@author: 삼성컴퓨터
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##가격이 lognormal이면 수익률을 normal
def invest_sim(N=100000):
    x=np.random.standard_normal((N,10))+np.ones((N,10))
    c=x.cumprod(axis=1)
    payoff_array=c[:,-1]-1
    return payoff_array
    
payoff_array = invest_sim()
print('AVG : ' + str(payoff_array.mean()))
print('STD : ' + str(payoff_array.std()))


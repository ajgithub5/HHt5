# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 01:20:29 2019

@author: AJAY
"""

import pandas as pd

prod = pd.read_csv("C:\\Users\\AJAY\\Documents\\HH Vietnam\\model_data1.csv")

prod.head()
prod['Product_1'].value_counts()
prod.dtypes
len(prod.columns)

prod[0:len(prod.rows),0:]



df = pd.get_dummies(prod[0:10])
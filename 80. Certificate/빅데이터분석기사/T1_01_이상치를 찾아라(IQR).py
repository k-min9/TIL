'''
작업형 1 문제 - 1. 이상치를 찾아라
데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_01_train.csv", encoding = 'utf-8')

# IQR 구하기
Q1 = np.percentile(df['Fare'], 25)
Q3 = np.percentile(df['Fare'], 75)
IQR = Q3 - Q1
# print('q', Q1, Q3, IQR)

# 이상치 구하기
df = df[(df['Fare'] < Q1 - 1.5*IQR)|(df['Fare'] > Q3 + 1.5*IQR)]
# 그 중에서 여성
df = df[df['Sex'] == 'female']

print(len(df))

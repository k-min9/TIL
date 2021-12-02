'''
작업형 1 문제 - 6. 결측치 제거 및 그룹 합계
주어진 데이터 중 
'f1'컬럼 결측 데이터를 제거하고, 
'city'와 'f2'을 기준으로 묶어 합계를 구하고, 
'city가 경기이면서 f2가 0'인 
조건에 만족하는 f1 값을 구하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

# f1 결측치 제거
df = df[~df['f1'].isnull()]
# print(df)

df2 = df.groupby(['city', 'f2']).sum()
# print(df2)

# 경기면서 f2가 0인 f1값
print(df2.iloc[0]['f1'])  

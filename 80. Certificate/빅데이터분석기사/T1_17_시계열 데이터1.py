'''
작업형 1 문제 - 17. 시계열 데이터1
2022년 5월 sales의 중앙값을 구하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic2.csv", encoding = 'utf-8')

# print(df['Date'])

# datetime으로 type 변경
df['Date'] = pd.to_datetime(df['Date'])
# print(df)
# print(df.info())  # object에서 datetime64로 바뀐것 확인 가능

# 아예 새로운 열 만들기
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month

# 조건 분리
answers = df[(df['year']==2022) & (df['month']==5)]
# print(answers)

print(answers['Sales'].median())
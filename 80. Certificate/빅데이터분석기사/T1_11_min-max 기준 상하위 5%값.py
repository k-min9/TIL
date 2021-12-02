'''
작업형 1 문제 - 11. min-max 기준 상하위 5%값
주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['f5'] = scaler.fit_transform(df[['f5']])  # 괄호 위치 갯수조심

# 하위 5% 값, 상위 5% 값
answer1 = df['f5'].quantile(0.05)
answer2 = df['f5'].quantile(0.95)

print(answer1 + answer2)
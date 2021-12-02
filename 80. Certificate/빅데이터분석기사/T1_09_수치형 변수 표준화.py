'''
작업형 1 문제 - 9. 수치형 변수 표준화
주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

# 이런 식으로 함수 체크
# from sklearn import preprocessing
# help(preprocessing)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df['f5'] = scaler.fit_transform(df[['f5']])  # 괄호 위치 갯수조심

# 중앙값 출력
print(df['f5'].median())
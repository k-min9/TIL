'''
작업형 1 문제 - 3. 결측치 처리(map 활용)
주어진 데이터에서 결측치가 20%이상 되는 컬럼은(변수는) 삭제하고, 
80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요!
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

# EDA
# print(df.isnull().sum())  # f1, f3 결측치 상황 각각 31% ,80%

# f3 컬럼 제거
df = df.drop(['f3'], axis=1)

# 도시별 중앙값
s = df[df['city']=='서울']['f1'].median()
k = df[df['city']=='경기']['f1'].median()
b = df[df['city']=='부산']['f1'].median()
d = df[df['city']=='대구']['f1'].median()

# f1 결측치 대체 (map 함수 사용)
#print(df)
df['f1'] = df['f1'].fillna(df['city'].map({'서울': s, '경기':k, '부산':b, '대구':d}))
#print(df)

# 최종 결과인 f1 컬럼값 출력
print(df['f1'].mean())
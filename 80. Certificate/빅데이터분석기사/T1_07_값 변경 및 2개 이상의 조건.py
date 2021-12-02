'''
작업형 1 문제 - 7. 값 변경 및 2개 이상의 조건
주어진 데이터 중 
'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 
'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오!
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

# 데이터 대체
df['f4'] = df['f4'].replace('ESFJ', 'ISFJ')

# 목표 데이터들
answers = df[(df['city'] == '경기') & (df['f4'] == 'ISFJ')]

# 중 age 컬럼 최대값
print(answers['age'].max())
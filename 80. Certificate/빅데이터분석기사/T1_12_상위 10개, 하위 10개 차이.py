'''
작업형 1 문제 - 12. 상위 10개, 하위 10개 차이
주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구하시오
(단, 100%가 넘는 접종률 제거, 소수 첫째자리까지 출력)
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_12_data.csv", encoding = 'utf-8')

# 정렬전 그룹화 (groupby에는 size sum max mean 같은것 다 올 수 있다.)
df = df.groupby('country').max()

# 우선 정렬
# help(df.sort_values)
df = df.sort_values(by='ratio' ,ascending=False)

# 상위, 하위 평균
answer1 = df['ratio'].head(10).mean()
answer2 = df['ratio'].tail(10).mean()
print(answer1 - answer2)
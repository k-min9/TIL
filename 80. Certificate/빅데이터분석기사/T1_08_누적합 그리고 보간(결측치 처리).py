'''
작업형 1 문제 - 8. 누적합 그리고 보간(결측치 처리) 
주어진 데이터 중 
 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산한다. 
 이때 발생하는 누적합 결측치는 바로 뒤의 값을 채우고, 누적합의 평균값을 출력한다. 
 (단, 결측치 바로 뒤의 값이 없으면 다음에 나오는 값을 채워넣는다)
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

# 결측치 먼저 메워야겠네
# help(df['f1'].fillna)
df['f1'] = df['f1'].fillna(method='backfill')

# 'f2' 컬럼이 1인 조건에 해당하는 데이터
answers = df[df['f2'] == 1]

# 누적합 계산
answers['f1'] = answers['f1'].cumsum()

# 누적합의 평균값
print(answers['f1'].mean())
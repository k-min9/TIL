'''
작업형 1 문제 - 2. 이상치를 찾아라(소수점)
주어진 데이터에서 이상치(소수점 나이)를 찾고 올림, 내림, 버림(절사)했을때 
3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오

import numpy as np
올림: np.ceil()
내림: np.floor()
버림: np.trunc()
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_02_data.csv", encoding = 'utf-8')
# print(df)

# 소수점 데이터 찾기
df = df[df['age'] - np.floor(df['age']) != 0]

# 올림, 내림, 버림 값
answer1 = np.ceil(df['age']).mean()
answer2 = np.floor(df['age']).mean()
answer3 = np.trunc(df['age']).mean()

print(answer1, answer2, answer3)
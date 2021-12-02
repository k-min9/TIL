'''
작업형 1 문제 - 5. 조건에 맞는 데이터 표준편차 구하기
주어진 데이터 중 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T1_00_basic1.csv", encoding = 'utf-8')

answers = df[df['f4'] == 'ENFJ']
answer1 = answers['f1'].std()

answers = df[df['f4'] == 'INFP']
answer2 = answers['f1'].std()

print(abs(answer2 - answer1))
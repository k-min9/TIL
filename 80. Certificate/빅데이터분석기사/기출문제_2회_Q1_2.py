'''
데이터셋에서 앞에서 순서대로 70%의 데이터만 활용해서
'f1' 컬럼 결측치를 중앙값으로 채우고, 전후의 표춘편차 차이 비교
'''
import pandas as pd
data = pd.read_csv('기출문제_2회_Q1.csv', encoding='utf-8')

# 위에서부터 70% (70개)
data = data.loc[:69]  # loc과 iloc은 스타팅넘버가 다른듯하다. (iloc은 .iloc[:70])
# len_val = int(0.7 * len(data)) 이런것도 가능하단거지
# data = data.iloc[:len_val]

# EDA : 결측치 확인 한 번 하고
# print(data.isnull().sum())

# 결측치 채우기 전 f1 컬럼 표준편차
answer1 = data['f1'].std()

# 중앙값으로 결측치 채우기
median_val = data['f1'].median()
data['f1'] = data['f1'].fillna(median_val)  # 이렇게 해당 열만 채울수도 있음

answer2 = data['f1'].std()

print(abs(answer2 - answer1))
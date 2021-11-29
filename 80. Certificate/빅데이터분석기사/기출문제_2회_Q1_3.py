'''
평균으로 부터 표준편차*1.5이상 벗어난 영역을 이상치라고 판단할때,
'age' 컬럼의 이상치를 전부 더하시오
'''
import pandas as pd
data = pd.read_csv('기출문제_2회_Q1.csv', encoding='utf-8')

chk = 1.5 * data['age'].std()
mean_val = data['age'].mean()

data_answer = data[(data['age'] > mean_val+chk) | (data['age'] < mean_val-chk)]
print(data_answer['age'].sum())
print(sum(data_answer['age']))
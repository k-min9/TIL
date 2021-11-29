'''
데이터셋의 f5 컬럼을 기준으로 상위 10개의 데이터를 구하고, 
10개 중 최소값으로 데이터를 대체한 후,
'age'컬럼에서 80이상인 데이터의 f5 컬럼 평균값 구하기
'''
import pandas as pd
data = pd.read_csv('기출문제_2회_Q1.csv', encoding='utf-8')

# f5컬럼 기준 상위 10개
data = data.sort_values('f5', ascending=False)


# f5 컬럼 10개중 최소값 (전부 같은 결과)
data2 = data.head(10)
min_val = min(data2['f5'])
#print(min_val)
min_val = min(data['f5'][:10])
#print(min_val)
min_val = data['f5'][:10].min()
#print(min_val)

# f5컬럼 기준 상위 10개의 값을 최소값으로 변경
data['f5'][:10] = min_val
#print(data)

# 'age'컬럼이 80이상인 데이터
data = data[data['age'] >= 80]
#print(data)

# 현재 데이터에서 'f5' 컬럼의 평균
print(data['f5'].mean())
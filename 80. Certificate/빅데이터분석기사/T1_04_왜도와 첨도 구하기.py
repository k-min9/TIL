'''
주어진 데이터 중 train.csv에서 'SalePrice'컬럼의 왜도와 첨도를 구한 값과, 
'SalePrice'컬럼을 스케일링(log1p)로 변환한 이후 왜도와 첨도를 구해 모두 더한 다음 소수점 2째자리까지 출력하시오
'''
import pandas as pd
import numpy as np

df = pd.read_csv("T2_04_data.csv", encoding = 'utf-8')

# 현재 왜도(s)와 첨도(k)
s1 = df['SalePrice'].skew()
k1 = df['SalePrice'].kurt()

# 컬럼 로그 변환
df['SalePrice'] = np.log1p(df['SalePrice'])

s2 = df['SalePrice'].skew()
k2 = df['SalePrice'].kurt()

print(round(s1+s2+k1+k2, 2))


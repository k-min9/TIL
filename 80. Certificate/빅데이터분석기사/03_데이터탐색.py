'''
1. 단변량 데이터 탐색 - 한 변수씩 데이터를 탐색
'''
import pandas as pd

data = pd.read_csv('03_데이터탐색_CEOSalary.csv', encoding='utf-8')
# data.info()  # 범주형 컬럼 개수와 자료 형태

# 1-1. 범주형 자료의 탐색
# 현 예시에서는 industry가 범주형 데이터
cnt = data['industry'].value_counts()  # 각 범주별 변수 빈도 파악
# print(cnt)
# 범주 데이터를 문자로 변형
data['industry'] = data['industry'].replace([1,2,3,4], ['서비스', 'IT', '금융', '기타'])  # 빼먹거나 일부만 하거나 오타 가능
# print(data)

# 1-2. 연속형 자료의 탐색
cnt = data.describe()  # 각 연속형 변수 요약 통계량, mean과 median이 비슷할 수록 이상치가 적다.
# print(cnt)
skew = data.skew()  # 왜도 (좌우 대칭이 아니고 치우친 정도, 정규분포 : 0)
# print(skew)
kurtosis = data.kurtosis()  # 첨도 (클수록 중앙에 몰림, 정규분포 : 0)

# 판다스 합, 평균, 중위 등 기본 함수
# help(data)

'''
2. 이변량 데이터 탐색 - 두 변수간의 탐색
'''
corr = data.corr()  # 디폴트 : pearson
# corr = data.corr(method="spearman")
# corr = data.corr(method="kendall") scipy 필요
# print(corr)

# 산업 범주별로 종속변수인 salary의 평균 및 기술통계량을 파악(groupby)
cnt = data.groupby('industry')[['salary']].describe()
# print(cnt)

'''
3. 이상치(outlier) 처리
'''
# 3-1. IQR 처리
Q1_salary = data['salary'].quantile(q=0.25)
Q3_salary = data['salary'].quantile(q=0.75)
IQR_salary = Q3_salary - Q1_salary
new_data = data[(data['salary'] < Q3_salary + IQR_salary*1.5) & (data['salary'] > Q1_salary - IQR_salary*1.5)]

Q1_sales = new_data['sales'].quantile(q=0.25)
Q3_sales = new_data['sales'].quantile(q=0.75)
IQR_sales = Q3_sales - Q1_sales
new_data = new_data[(new_data['sales'] < Q3_sales + IQR_sales*1.5) & (new_data['sales'] > Q1_sales - IQR_sales*1.5)]

new_corr = new_data.corr()
# print(corr)
# print('---')
# print(new_corr)  # 상관 계수가 증가한 것 확인 가능

'''
4. 변수 변환
'''
# 4-1. 로그 변환 열 추가 (넘파이 필요) - 이것만으로도 왜곡 관계는 많이 해결 됨
import numpy as np
data['log_salary'] = np.log(data['salary'])
data['log_sales'] = np.log(data['sales'])
data['log_roe'] = np.log(data['roe'])

# 4-2 제곱근 변환 열 추가
data['sqrt_salary'] = np.sqrt(data['salary'])
data['sqrt_sales'] = np.sqrt(data['sales'])
data['sqrt_roe'] = np.sqrt(data['roe'])

'''
5. 결측치 처리
'''
data = pd.read_csv('03_데이터탐색_Missing.csv')
#print(data)
#print(data.isnull().sum())

# 5-1. 결측값 확인 : pd.isnull(data) or data.isnull().sum()
# 기타 파이썬 같은 방법
null_cnt = 0
for d in data['salary']:
    if d != d:  # float('nan')은 이게 False 나옴
        null_cnt += 1
# print(null_cnt)

# 결측치 존재 여부 체크용 행 만들기
data['missing'] = data.isnull().sum(1)  # 행 단위로 체크하여 nan, null 있으면 1씩 증가
data['valid'] = data.notnull().sum(1)  # 행 단위 체크하여 값이 존재할 경우 1씩 증가

# 5-2. 결측값 제거 : dropna()
data2 = data.dropna()  # 결측값 있는 행 제거, axis=0 기본값이라 생략 가능
data3 = data.dropna(axis=1)  # 결측값 있는 열 제거
# print(data3)

# 5-3. 결측값 대체 : fillna()
data4 = data.fillna(0)  # 결측값 0으로 대체
data4 = data.fillna({'salary':0, 'sales':1})  # 특정 열만 대체 + 다르게 대체하는 방법
data5 = data.fillna('빈값')  # 결측값 문자열로 대체
data6 = data.fillna(method='ffill')  # 앞의 값으로 채우기(pad도 동일), 앞 값이 없으면 NaN
data7 = data.fillna(method='bfill')  # 앞의 값으로 채우기(pad도 동일),  뒤 값이 없으면 NaN
data8 = data.fillna(data.mean())  # 평균 mean, 중위값 median, 최대값 max 뭐 이것저것.. 괄호 빼먹지 말자!
data9 = data.fillna(data.mean()['salary'])  # 남의 평균으로 메우기
# print(data9)

# 5-3-2. 결측값 대체 심화
data = pd.read_csv('03_데이터탐색_Missing.csv')  # 재선언
data2 = data.copy()

# where 절로 3항 연산자 하듯이
data2['sales_new'] = np.where(pd.notnull(data2['sales']) == True, data2['sales'], data2['salary'])  # 내용 있으면 sales 없으면 salary 수치 넣기
#print(data2)

# 람다 함수와 apply 이용
fill_values = {1: 1000, 2: 2000}  # 집단별로 변경할 값 설정
fill_func = lambda d: d.fillna(fill_values[d.name])  # lamda 함수 적용
data3 = data.groupby('industry').apply(fill_func)  # industry 값에 맞춰 메우기
# print(data3)

# 변수별 다른 대체 방법
data_filter = {'salary': data.salary.interpolate(),  # 보간법
                'sales': data.sales.mean(),  # 평균
                'roe': 'missing'}  # 문자열
data4 = data.fillna(data_filter)
# print(data4)
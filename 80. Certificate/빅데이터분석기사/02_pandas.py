'''
pandas : Panel Data Set, 엑셀 같은 정형 데이터(DataFrame)를 파이썬에 2차원으로 불러오고, joining, merging, reshaping
자료구조 및 데이터 분석 처리를 위한 핵심 패키지, 데이터를 판다스 형태로 불러와 데이터를 확인하고 분석을 수행하며, 크게 Series와 DataFrame의 형태로 나눌 수 있음
1D : series, 2D : DataFrame, 3D : Panel
(설치 : pip install pandas)
'''
import pandas as pd
#print(dir(pd))

# 1D : Series = 인덱스(기본 0부터 시작하는 숫자 바꿀 수 있음)와 값이 쌍을 이룸
a = pd.Series([1, 2, 3, 4])
# print(a)
# print('값 : ', a.values)
# print('인덱스 : ', a.index)

# 2D : DataFrame에 파일 불러오기
df = pd.read_csv('02_pandas_GrapeData.csv')
# df = pd.read_csv('02_pandas_GrapeData.csv', encoding='euc-kr') : 한글 깨질 경우
# print(df)
# df = pd.read_excel('02_pandas_GrapeData.xlsx')  # 엑셀일 경우 openpyxl 필요하지만, 제공 패키지 리스트에도 없으니까 패스

# DataFrame 슬라이싱
a = df.head(3)  # 앞에서 3개
b = df.tail(4)  # 뒤에서 4개
c = df[1:4]  # 1에서 3까지
# print(a)
# print(b)

# 열 조회
d1 = df['price']  # 형태 : Series
d2 = df[['price']]  # 형태 : DataFrame
d3 = df.price  # d1과 동일. 형태 : Series
d4 = df[df.columns[[0, 2, 4]]]  # 0열, 2열, 4열. 형태 : DataFrame, # columns : 열 이름 확인
# print(d1)
# print(d4)

# loc, iloc, at
i1 = df.loc[:, 'continent':'size']  # continent 열에서 size 열까지
i2 = df.iloc[1:7, 0:2]  # 1~7행 0~2열
i3 = df.at[5, 'price']  # 5행 'price'열(숫자 안 됨)
# print(i1)
# print(i3)


# 데이터 변환 : 복사, 추가, 삭제
df2 = df.copy()  # 복사
df2 = df[['size', 'period', 'price']]  # 열 필터링
df2.rename(columns={'period': 'time'}, inplace=True)  # 열 이름 변경 : period->time으로 바꾸고 뒤집어쓰기(inplace) 
df2['growth']=df2['size']/df2['time']  # 열 추가. 계산 불가(빈 값 들어갈 경우)면 에러 발생
# print(df2)
del df2['growth']
# print(df2)

# 데이터 추출
df3 = df[(df['continent']==1) & (df['brand']==1)]   # continent가 1이고, brand가 1인 데이터 추출
df3 = df[(df['size']>=10) | (df['period']>=30)]  # size가 10 이상이거나, period가 30이상인 데이터 추출
# print(df3)

# 데이터 일괄 변경 (brand 1,2를 1로 brand 3을 2로)
# 방법 1 : df.replace({"brand":{1:1, 2:1, 3:2}})
# 방법 2 : 함수 정의, df.apply(함수)
def brand_grouping(series):
    if series <= 2:
        return 1
    else:
        return 2
df2 = df.copy()
df2['brand'] = df2['brand'].apply(brand_grouping)  # df2['brand_new'] 등으로 쓰면 새로운 열 추가하면서 거기 표기(기존 열 유지)
# print(df2)
# print(df2['brand'].value_counts())  # 범주 간 내용 체크

'''
판다스와 넘파이
판다스 : 내용 확인이 쉬움, 느림  -> 파일 읽기, 기본적 분석
넘파이 : 내용 확인이 어려움, 빠름  -> 머신러닝, 딥러닝 등 오래걸리는 연산 수행
서로 쉽게 변환되므로, 변환해가며 보완하는 관계
'''
import numpy as np

# 판다스 -> 넘파이
df_np = df.to_numpy()
# print(df_np)  # 변수 설명 없이 array가 쭉 나열

# 넘파이 -> 판다스
df_pd = pd.DataFrame(df_np)
# print(df_pd)  # 변수 설명에 0, 1, 2, 3, 4가 표기됨...

# 넘파이 -> 판다스 (변수 설명)
df_pd2 = pd.DataFrame(data=df_np, columns=['a', 'b', 'c', 'd', 'e'])  # column 수 모자라면 에러 발생
print(df_pd2)
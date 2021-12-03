# 빅데이터 분석기사(실기) 요약

## 단답형

키워드 바구니

```
DIKW 피라미드 : 데이터 정보 지식 지혜
클라우드 컴퓨팅
빅데이터 플랫폼
- 수집 : 크롤러(비정형), EAI
- 저장 : RDBMS, NoSQL
인포그래픽 : info + graphic
- 히스토그램 : 직사각형
비지도 학습 : 사람의 개입이 필요 없음, 입력에 대한 정답(Label)이 없음, 입력들의 규칙성 찾기, 상향식 접근방법, 딥러닝(신경망모델)
지도 학습 : 훈련 데이터로부터 하나의 함수를 유추해감.
- 지도학습 변수 선택 : 필터, 래퍼, 임베디드
개인정보보호법
빅데이터 분석 방법론 : 단계 태스크 스텝, KDD, CRISP-DM
데이터 수집
- 정형(스키마, 구조, 컬럼) : ETL(Extract Transform Load) , FTP(File Transfer Protocol), API, ERP
- 비정형 : 크롤링, Open API, 스크래파이(파이썬), 아파치 카프카(분산)
- 반정형 : XML : 특수 다목적 마크업 언어 / JSON : 키-값
데이터 웨어하우스, 데이터 마트
기계학습(머신 러닝) : 인간과 같은 학습 능력을 기계로 구현, 역전파 알고리즘으로ㅓ 안정화
회귀분석 : 연속형 변수들에 대해 두 변수사이의 모형을 구하고, 적합도를 측정하는 분석 방법(연령대 - 구매상품종류 및 특성)
전처리 : 결측값, 이상값(IQR), 노이즈(입력되지 않았는데 입력되었다고 착각)
단순대치 : 완전분석, 평균대치 / 핫덱 대체, 콜드덱 대체 => 다중대치 : 대치->분석->결합
차원의 저주(정보밀도) -> 해결 : 차원축소 , 과(대)적합(학습데이터 특화)
비닝(Binning) : 데이터 분할 계산, 데이터 평활화
EDA : 탐색적 데이터 분석
시각적 데이터 : 히스토그램, 막대형 그래프, 박스 플롯, 산점도
상관분석 : 수치적데이터(피어슨 상관계수, -1 ~ 1), 명목적데이터(카이검정), 순서적데이터(스피어만 상관계수)
왜도 : 0보다 작음 => 좌측으로 긴 꼬리(왼쪽 편포) ; ㅈㅈ
분산분석 : ANOVA
데이터 마이닝 : 분류, 예측, 군집화, 연관규칙(장바구니)
자기 조직화 지도(SOM) : 입력층/결정층, 인공신경망 
회귀분석(결정계수,R), 의사결정나무(CART-이진트리형태), 인공신경망(퍼셉트론), 서포트벡터머신
의사결정나무 분류 규칙 : 카이제곱 통계량, 지니지수, 엔트로피지수
딥러닝 : DNN(deep), CNN(convolution), RNN(regression)
텍스트 마이닝
사회연결망
앙상블 : 샘플링(배깅(Bootstrap Aggregating)-보팅/부스팅-가중치), 변수(랜덤포레스트-무작위성)
향상도, 맨하튼거리
평가지표
- 회귀 모형 : SSE, SST, SSR, R
- 분류 모형 : 혼동행렬, ROC 곡선의 AUC
교차검증
```

- 기타

> 은닉계층 값 계산해보기



## 작업형

### 작업형 1

기본 함수

```
print(dir())
help()
```

numpy 함수

```
np.ceil(df['age'])  # 올림
np.floor(df['age'])  # 내림
np.trunc(df['age'])  # 버림
```

pandas 함수

```
# 선택
i0 = df[1:4]  # 1에서 3까지
i1 = df.loc[:, 'continent':'size']  # continent 열에서 size 열까지
i2 = df.iloc[1:7, 0:2]  # 1~7행 0~2열
i3 = df.at[5, 'price']  # 5행 'price'열(숫자 안 됨)

.head(n)  # 상위 n개
.tail(n)  # 하위 n개

# 기본 함수
.mean()  # 평균
.median()  # 중앙값
.mode()  # 최빈
.std() # 표준편차
.max()/ .min()  # 최대, 최소
.skew()  # 왜도
.kurt()  # 첨도

- 시계열 관련
df['Date'] = pd.to_datetime(df['Date'])  #datetime으로 type 변경
df['year'] = df['Date'].dt.year  # 새로운 'year'열 만들기 (정수 비교 가능)
df['month'] = df['Date'].dt.month  # 새로운 'month'열 만들기  (정수 비교 가능)
```

사용자 함수 적용

```
X1['gender'] = X1['gender'].apply(change_gender)
```

정렬 함수

```
df = df.sort_values(by='ratio' ,ascending=False)
```

그룹 함수

```
df = df.groupby('country').max()
df2 = df.groupby(['city', 'f2']).sum()
```

나누기

```
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)
```

IQR

```
Q1_salary = data['salary'].quantile(q=0.25)  # 아니면 np.percentile(df['salary'], 25)
Q3_salary = data['salary'].quantile(q=0.75)  # 아니면 np.percentile(df['salary'], 75)
IQR_salary = Q3_salary - Q1_salary
```

컬럼 삭제

```
X_train = X_train.drop(['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender'], axis=1)
```



### 작업형 2

#### 기본 전략

종속변수가 0, 1범주형이면 로지스틱 회귀, 그 외는 전부 랜덤 포레스트로 접근

일단 시간 남으면 둘 다 쓰고 train score 높은 쪽으로 제출

```
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
```



#### 이론 체크

결측치 확인

```
print(X_train.isnull().sum()) # 전체 확인
data['missing'] = data.isnull().sum(1)  # 행 단위 체크 열 만들기
```

결측치 제거

```
data2 = data.dropna()  # 행 제거
data3 = data.dropna(axis=1)  # 열 제거

# f1이 결측치가 있을경우 그 행 삭제
df = df[~df['f1'].isnull()]

# 특정 열 삭제
X_test = X_test.drop(columns=[id_name, target])

# 특정 행(포도당(Glucose)이 0인 행) 삭제
del_idx = X_train[(X_train['Glucose'] == 0)].index
X_train = X_train.drop(index=del_idx, axis=0)
y_train = y_train.drop(index=del_idx, axis=0)
```

결측치 대체

```
data4 = data.fillna(0)  # 결측값 0으로 대체
data4 = data.fillna({'salary':0, 'sales':1})  # 특정 열만 대체 + 다르게 대체하는 방법
data5 = data.fillna('빈값')  # 결측값 문자열로 대체
data6 = data.fillna(method='ffill')  # 앞의 값으로 채우기(pad도 동일), 앞 값이 없으면 NaN
data7 = data.fillna(method='bfill')  # 앞의 값으로 채우기(pad도 동일),  뒤 값이 없으면 NaN
data8 = data.fillna(data.mean())  # 평균 mean, 중위값 median, 최대값 max 뭐 이것저것.. 괄호 빼먹지 말자!
data9 = data.fillna(data.mean()['salary'])  # 남의 평균으로 메우기
data['f1'] = data['f1'].fillna(median_val)  # 이렇게 해당 열만 채울수도 있음
df['f1'] = df['f1'].fillna(df['city'].map({'서울': s, '경기':k, '부산':b, '대구':d}))  # map 함수 사용
```

이상치 대체

```
# 모든 0을 평균 값으로 변경
cols = ['BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
cols_mean = X_train[cols].mean()
X_train[cols] = X_train[cols].replace(0, cols_mean)
```

원 핫 인코딩

```
X1_dummy = pd.get_dummies(X1)
```

레이블 인코더

```
cat_features = [
                 'workclass',              
                 'education',            
                 'marital.status', 
                 'occupation', 
                 'relationship', 
                 'race', 
                 'sex',
                 'native.country'
]

from sklearn.preprocessing import LabelEncoder

# 합쳐서 레이블 인코더
all_df = pd.concat([X_train.assign(ind="train"), X_test.assign(ind="test")])
le = LabelEncoder()
all_df[cat_features] = all_df[cat_features].apply(le.fit_transform)

# 끝나고 다시 train과 test로 나누기 (미리 위에서 ind열을 만들어서 train과 test를 나눠뒀었음)
X_train = all_df[all_df['ind'] == 'train']
X_train = X_train.drop('ind',axis=1)

X_test = all_df[all_df['ind'] == 'test']
X_test = X_test.drop('ind',axis=1)
```

레이블 범주화

```
# target값 변경
y = (y_train['income'] != '<=50K').astype(int) # 50 이하면 1 아니면 0으로 변경 됨
```

정규화

```
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()  # 학습기 세팅
1. 차근차근
scaler.fit(X_train)  # 학습
X_train_new = scaler.transform(X_train)
X_test_new = scaler.transform(X_test)  # 여기는 fit 하면 안된다!

2. 아니면 한방에 
X_train_MINMAX = scaler_MINMAX.fit_transform(X_train)
X_test_MINMAX = scaler_MINMAX.transform(X_test)  # 여기는 fit 하면 안된다!

결과물은 ndarray임
```

모델 학습

```
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_MINMAX, Y_train)
pred_train = model.predict(X_train_MINMAX)  # predict : 예측결과
pred_train_proba = model.predict_proba(X_train_MINMAX)  # predict_proba : 범주 1이 나올 확률
```

결과 출력

```
1. 결과물 만들기
answer = pd.DataFrame({
    'ID' : y_test['ID'],
    'Reached.on.Time_Y.N' : pred
})

2. 기존결과물에 합치기
answers = pd.concat([X_test, Y_test], axis = 1)  # 열로 조합

파일화
answers.to_csv('answers.csv', index=False)
```

정확도 체크

```
score = model.score(X_train, Y_train)
```




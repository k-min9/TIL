'''
6. 데이터 정제 실전과제
'''
import pandas as pd

data=pd.read_csv('04_데이터정제_house_raw.csv', encoding='utf-8')

# 목적 : 주택가격 예측 >> 선형회귀분석 사용
X = data[data.columns[0:5]] # X축에 housing_age에서 rooms까지 입력
Y = data[["house_value"]]

# 학습용 데이터와 테스트 데이터 구분 (7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)  # random_state : 시드값 

# 변수 단위 통일(Min Max Scaler)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()  # 학습기 세팅
scaler.fit(X_train)  # 학습
X_train_new = scaler.transform(X_train)
X_test_new = scaler.transform(X_test)

# 선형 회귀 라이브러리
from sklearn.linear_model import LinearRegression
model = LinearRegression()  # 모델 세팅
model.fit(X_train_new, Y_train) # 학습

# 훈련 데이터 정확도(R)
score = model.score(X_train_new, Y_train)
# print(score) # 0.54 나름 정확

# 실제 데이터 정확도
score = model.score(X_test_new, Y_test)
# print(score) # 정확도 -2.82.... 난리 남
# >> 이유는 이상치!


'''
이상치 판단 기준은 주관적이지만 예시대로 정제
'''
data2 = data[(data['bedrooms']<0.5) & (data['households']<7) & (data['rooms']<12)]
X = data2[data2.columns[0:5]]
Y = data2[["house_value"]]

# 위와 같은 내용 실행
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)

scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_new = scaler.transform(X_train)
X_test_new = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
model = LinearRegression()  # 모델 세팅
model.fit(X_train_new, Y_train) # 학습

score1 = model.score(X_train_new, Y_train)
score2 = model.score(X_test_new, Y_test)

print('score : ', score1, score2) # 57%, 58%로 우수히 정제된것을 확인
'''
머신러닝의 전반적인 프로세스
1. Data Set 분할 : '학습(/검증) 70~80%, 테스트 셋 20~30%'로 분리 (일반적으로, 검증은 최종 분류에 사용되지 않음!)
2. 전처리과정 : 정규화, MinMax 정규화, 범주형 데이터는 우선 0과 1로 나눈다.(one-hot-encoding)
3. 모델 적용 : 알고리즘에 데이터를 적용(fit) / 레이블이 존재한다면 지도학습(연속-회귀, 범주-분류) 아니면 군집이나 연관분석
4. 모델 튜닝 : hyper parameter 탐색 및 최종 모델 결정
5. 모델 평가 : 회귀-R, RMSE, 분류-오차행렬
'''
# 1. 자료 읽기
import pandas as pd
data=pd.read_csv('06_ML프로세스_예시2_회귀문제_house_price.csv', encoding='utf-8')

# 자료 설명 : 목적 변수 : 'class', 유방암 여부 이진(0/1) 데이터
# print(data)

# 2. 특성(x)과 레이블(y) 나누기
# X = data[['이름1','이름2',...]]  # 방법 1
X = data[data.columns[0:5]]  # 방법 2 : 연달아있으면 오타도 없고 이게 편함, 떨어져 있으면 # X = data[data.columns[[0,2,4]]]
Y = data[["house_value"]]

# 3. Data Set 분할
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42)  # stratify : 범주 비율 맞추기(회귀는 y가 범주가 아니니까 사용불가!), random_state : 시드 값

# 4. 정규화 : 특성치 단위 맞추기 (민맥스, 표준화 둘 다 예시)
from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler_MINMAX = MinMaxScaler()
scaler_MINMAX.fit(X_train)
X_train_MINMAX = scaler_MINMAX.transform(X_train)
X_test_MINMAX = scaler_MINMAX.transform(X_test)

scaler_STD = StandardScaler()
scaler_STD.fit(X_train)
X_train_STD = scaler_STD.transform(X_train)
X_test_STD = scaler_STD.transform(X_test)

# 5. 모델 학습 (예시 - 선형 회귀 모델)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_MINMAX, Y_train)
pred_train = model.predict(X_train_MINMAX)  # predict : 예측결과
pred_test = model.predict(X_test_MINMAX)
score = model.score(X_train_MINMAX, Y_train)  # score : 정확도 
# print(score)

# MSE 등을 사용하여 틀린정도를 확인 가능
# from sklearn.metrics import mean_squared_error
# MSE = mean_squared_error(Y_test, pred_test)
# print(MSE**0.5)

print(type(Y_test))

# 6. 예측값 병합 및 저장 [작동체크]
Y_test[['y_pred']] = pred_test

answers = pd.concat([X_test, Y_test], axis=1)  # 열로 조합
answers.to_csv('new_data.csv')
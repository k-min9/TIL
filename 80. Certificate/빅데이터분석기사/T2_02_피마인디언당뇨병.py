'''
작업형 2 문제 - 2. 피마인디언당뇨병
당뇨병 여부 판단
'''
# 입력
'''원래는 주어지는 데이터 읽어오기임 환경 조절 중'''
# 시험환경 세팅 (코드 변경 X)
import pandas as pd
df = pd.read_csv("T2_02_data.csv")

from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=2021)
y_train = X_train['Outcome']
X_train = X_train.drop(columns=['Outcome'])
y_test = X_test['Outcome']
X_test = X_test.drop(columns=['Outcome'])
'''여기까지'''
# 실제로는 이런 느낌
# import pandas as pd

# X_test = pd.read_csv("data/X_test.csv")
# X_train = pd.read_csv("data/X_train.csv")
# y_train = pd.read_csv("data/y_train.csv")



# EDA
# print(X_train.isnull().sum())  # 결측치 없는 클린한 데이터

# 데이터 전처리 >> 값이 0인 이상치가 너무 많음
# 1. train만 0이 있는 포도당(Glucose) 0인 행 삭제
del_idx = X_train[(X_train['Glucose'] == 0)].index
X_train = X_train.drop(index=del_idx, axis=0)
y_train = y_train.drop(index=del_idx, axis=0)

# 2. 포도당을 제외한 이상치는 전부 평균값으로 대체
cols = ['BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
cols_mean = X_train[cols].mean()
# print(cols_mean)
X_train[cols] = X_train[cols].replace(0, cols_mean)

# 정규화
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
scaler.fit(X_test)
X_test_scaled =scaler.transform(X_test)

# 모델 적용
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
pred = model.predict(X_test_scaled)
#print(pred)

# 결과물 확인 및 출력
answers = pd.DataFrame({
    'idx' : y_test.index,
    'Outcome' : pred
})
print(answers)
answers.to_csv('answers.csv', index=False)
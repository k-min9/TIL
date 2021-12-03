'''
작업형 2 문제 - 0. 입문용 및 테스트
생존 여부 예측 모델 만들기
'''
# 입력
import pandas as pd

X_test = pd.read_csv("T2_00_X_test.csv", encoding= 'utf-8')
X_train = pd.read_csv("T2_00_X_train.csv", encoding='utf-8')
y_train = pd.read_csv("T2_00_y_train.csv", encoding='utf-8')


# EDA 
# print(X_train.info())
# print(X_train)
# print(X_train.isnull().sum())
# print(X_test.isnull().sum())

# 여차하면 수치형 데이터만 선택
X_train = X_train.select_dtypes(exclude='object')
X_test = X_test.select_dtypes(exclude='object')

# ID 제거
X_train = X_train.drop('enrollee_id', axis=1)
X_test = X_test.drop('enrollee_id', axis=1)

# 스케일링
from sklearn.preprocessing import MinMaxScaler
# print(X_train)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# 모델 적용 (help 연습하면서 ㄱㄱㄱ)
# import sklearn
# from sklearn import ensemble
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
# print(dir(model))
# help(model)
model.fit(X_train_scaled, y_train['target'])
pred = model.predict(X_test_scaled)

# 출력 전 enrollee_id 날려버려서 다시 불러옴...
X_test = pd.read_csv("T2_00_X_test.csv", encoding= 'utf-8')
answers = pd.DataFrame({
    'enrollee_id' : X_test.enrollee_id,
    'target' : pred
})

# 출력
# print(answers)
answers.to_csv('answers.csv', index=False)

# 채점
import pickle
from sklearn.metrics import roc_auc_score

with open( "T2_00_answer.pickle", "rb" ) as file:
    ans = pickle.load(file)
    ans = pd.DataFrame(ans)
print(roc_auc_score(ans['target'], pred))
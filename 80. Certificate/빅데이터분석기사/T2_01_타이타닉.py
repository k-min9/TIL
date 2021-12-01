'''
작업형 2 문제 - 1. 타이타닉
생존 여부 예측 모델 만들기
'''
# 입력
'''원래는 주어지는 데이터 읽어오기임 환경 조절 중'''
# 시험환경 세팅 (코드 변경 X)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def exam_data_load(df, target, id_name="", null_name=""):
    if id_name == "":
        df = df.reset_index().rename(columns={"index": "id"})
        id_name = 'id'
    else:
        id_name = id_name
    
    if null_name != "":
        df[df == null_name] = np.nan
    
    X_train, X_test = train_test_split(df, test_size=0.2, shuffle=True, random_state=2021)
    y_train = X_train[[id_name, target]]
    X_train = X_train.drop(columns=[id_name, target])
    y_test = X_test[[id_name, target]]
    X_test = X_test.drop(columns=[id_name, target])
    return X_train, X_test, y_train, y_test 
    
df = pd.read_csv("T2_01_train.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Survived', id_name='PassengerId')
'''여기까지'''
# 실제로는 이런 느낌
# import pandas as pd

# X_test = pd.read_csv("data/X_test.csv")
# X_train = pd.read_csv("data/X_train.csv")
# y_train = pd.read_csv("data/y_train.csv")



# 데이터 전처리
y = y_train['Survived']

# get_dummies로 원 핫 인코딩(이거 하기 전에 숫자 변경 등 없음, sex만 웟 핫 인코딩 될 예정)
features = ["Pclass", "Sex", "SibSp", "Parch"]
X_train = pd.get_dummies(X_train[features])
X_test = pd.get_dummies(X_test[features])

# 모델 및 평가
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y)
# print(model.score(X_train, y))  # 81.6

pred = model.predict(X_test)  # 아직 ndarray

answers = pd.DataFrame({
    'PassengerId': y_test.PassengerId, 
    'Survived': pred
    })

answers.to_csv('answers.csv', index=False)
# print(model.score(X_test, y_test['Survived']))  # 73.18
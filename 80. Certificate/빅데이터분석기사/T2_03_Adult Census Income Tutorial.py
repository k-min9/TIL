'''
작업형 2 문제 - 3. Adult Census Income Tutorial
성인 인구조사 소득 예측
(https://www.kaggle.com/agileteam/t2-3-adult-census-income-tutorial)
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
    
df = pd.read_csv("T2_03_data.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='income', null_name='?')
'''여기까지'''
# 실제로는 이런 느낌
# import pandas as pd

# X_test = pd.read_csv("data/X_test.csv")
# X_train = pd.read_csv("data/X_train.csv")
# y_train = pd.read_csv("data/y_train.csv")




# EDA
# print(X_train.isnull().sum())

# 피쳐 구분 (숫자, 카테고리)
numeric_features = [
                    'age',
                    'fnlwgt', 
                    'education.num',
                    'capital.gain', 
                    'capital.loss', 
                    'hours.per.week',                     
                   ]
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

# 데이터 전처리
# 결측치 : 최빈값과 차이가 크면 최빈값으로 값이 비슷하면 별도의 값으로
def data_fillna(df):
    df['workclass'] = df['workclass'].fillna(df['workclass'].mode()[0])  # private
    df['occupation'] = df['occupation'].fillna("null")
    df['native.country'] = df["native.country"].fillna(df['native.country'].mode()[0])  # United-States
    return df

# print(X_test['native.country'].mode()[0])
X_train = data_fillna(X_train)
X_test = data_fillna(X_test)

#  피처 엔지니어링 (레이블 인코더)
# print(X_train)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()  
X_train[cat_features] = X_train[cat_features].apply(le.fit_transform)  # 문자 범주를 숫자로 변경
X_test[cat_features] = X_test[cat_features].apply(le.fit_transform)
# print(X_train)
# print(X_test)

# 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])
X_test[numeric_features] = scaler.transform(X_test[numeric_features])  # 여기는 fit 하면 안 됨!!

# target값 변경
y = (y_train['income'] != '<=50K').astype(int)
# print(y)


# 모델 & 평가
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y)
pred = model.predict(X_test)
print(model.score(X_train, y))

answers = pd.DataFrame({
    'idx' : y_test.index,
    'income' : pred
})
print(answers)
answers.to_csv('answers.csv', index=False)

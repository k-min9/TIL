'''
제품 배송시간에 맞춰 배송되었는지 예측모델 만들기

학습용 데이터 (X_train, y_train)을 이용하여 배송 예측 모형을 만든 후, 
이를 평가용 데이터(X_test)에 적용하여 얻은 예측값을 다음과 같은 형식의 CSV파일로 생성하시오(제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점)

(유의사항)

1.성능이 우수한 예측모형을 구축하기 위해서는 적절한 데이터 전처리, 피처엔지니어링, 분류알고리즘, 하이퍼파라미터 튜닝, 모형 앙상블 등이 수반되어야 한다.
2.수험번호.csv파일이 만들어지도록 코드를 제출한다.
3.제출한 모델의 성능은 ROC-AUC형태로 읽어드린다.
'''
import pandas as pd
data = pd.read_csv('기출문제_2회_Q1.csv', encoding='utf-8')


# 입력
'''원래는 주어지는 데이터 읽어오기임 환경 조절 중'''
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
    
df = pd.read_csv("기출문제_2회_Q2.csv")
X_train, X_test, y_train, y_test = exam_data_load(df, target='Reached.on.Time_Y.N', id_name='ID')
'''여기까지'''
# 실제로는 이런 느낌
# X_test = pd.read_csv("data/X_test.csv")
# X_train = pd.read_csv("data/X_train.csv")
# y_train = pd.read_csv("data/y_train.csv")

''' 풀이 시작 '''

# 레이블(타겟, y) 확인
# print(y_train)
# print(y_train['Reached.on.Time_Y.N'].value_counts())

# 결측치 확인  >> 없음
# print(X_test.isnull().sum())

# 타입 컬럼, 고유값 개수 확인 코드
# print(X_train.nunique())

# 필요없어보이는 컬럼 삭제(또는 라벨 인코딩, 원 핫 인코딩) 및 형태 맞추기
X_train = X_train.drop(['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender'], axis=1)
X_test = X_test.drop(['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender'], axis=1)
y_train = y_train[['Reached.on.Time_Y.N']]
#print(y_train)

### 모델 및 평가 (이중에 골라잡기)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 예시 1 - 로지스틱 회귀 (다른 모델도 죄다 fit->predict로 동일)
model = LogisticRegression()
model.fit(X_train, y_train)

# 모델 적용
pred = model.predict(X_test)  # ndarray 형태로 반환

# 정답 및 출력
answer = pd.DataFrame({
    'ID' : y_test['ID'],
    'Reached.on.Time_Y.N' : pred
})

# 답안 제출
answer.to_csv('003000000.csv', index=False)

# 스코어 확인
print(round(model.score(X_test, y_test['Reached.on.Time_Y.N']) * 100, 2))



'''
+@ 정규화 해보자
'''
from sklearn.preprocessing import MinMaxScaler
scaler_MINMAX = MinMaxScaler()
scaler_MINMAX.fit(X_train)
X_train_MINMAX = scaler_MINMAX.transform(X_train)
X_test_MINMAX = scaler_MINMAX.transform(X_test)

model = LogisticRegression()
model.fit(X_train_MINMAX, y_train)
pred = model.predict(X_test_MINMAX) 

# 정답 및 출력
answer = pd.DataFrame({
    'ID' : y_test['ID'],
    'Reached.on.Time_Y.N' : pred
})

# 답안 제출
answer.to_csv('003000000.csv', index=False)

# 스코어 확인
print(round(model.score(X_test_MINMAX, y_test['Reached.on.Time_Y.N']) * 100, 2))
'''
점수변동 그다지 없었음
'''

'''
정규화 : 특성치(X)의 단위를 동일하게!
'''
import pandas as pd
data = pd.read_csv('07_ML프로세스_2_데이터셋분할과모델검증_vote.csv', encoding='utf-8')

# 특성치(X) 나누기 (같은 구현 타입 세 종류)
# X = data[['gender_female', 'gender_male', ...]]
X = data[data.columns[1:14]]
X = data.loc[:, 'gender_female':'score_intention']

# 레이블(y) 정하기
y = data[['vote']]

# 데이터 셋 train, test나누고
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

# 연속형 특성의 스케일링 
# 1. Min-Max Scaling (MinMax로 최소 최대가 0~1인 데이터로 표현하는 방식)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)  # fit로 정규화 기준 적용 (아직 정규화 안한 상태!)
X_train_scaled = scaler.transform(X_train)  # 이후는 transform으로 정규화 적용

#print(X_train_scaled)
#print(pd.DataFrame(X_train_scaled).describe())  # 자료 확인용

# 2. Standardization Scaling (표준화로 평균 0 표준편차 1로 통일하는 방식)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

## 이 상태에서 LinearRegresssion을 적용하면 더 높은 적합도를 보인다.



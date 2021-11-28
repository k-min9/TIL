'''
훈련 데이터와 테스트데이터를 나누는 기본적인 방법 외에
교차검증과 검증데이터를 별도로 두는 방법등을 살펴보자.
'''
# 경고 무시 파이썬 명령어
# import warnings
# warnings.filterwarnings("ignore")

import pandas as pd
data = pd.read_csv('07_ML프로세스_2_데이터셋분할과모델검증_vote.csv', encoding='utf-8')
# print(data)

# 특성변수 데이터셋 나누기
X = data[data.columns[1:14]]  # 아니면 전부 쓰는게 내 취향

# 투표변수를 y로
y = data[['vote']]
print(y)

# train과 test를 7:3으로 나누는게 기본이고, 그렇게 하지만, 만약 바꾸고 싶으면 옵션 train_size=0.8
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, stratify=y, random_state=42)

# 이번에는 정규화 없이 진행

# LogisticRegression 알고리즘 가져와서 model이라는 이름으로 모델 적용
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

'''
교차검증 - 테스트 데이터를 그룹화하고 나눠서 특정 그룹만 빼고 테스트한다던가 하는 방식으로 비교 검증
랜덤없는 교차검증 : from sklearn.model_selection import cross_val_score
랜덤있는 교차검증 : from sklearn.model_selection import KFold
임의분할 교차검증 : from sklearn.model_selection import ShuffleSplit

이 부분 생략
'''

# train data를 train과 valid data로 나누기 : train_test_split을 두 번 적용
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train)

# 모델 훈련
model.fit(X_train, Y_train)



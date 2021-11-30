'''
하이퍼 파라미터(C)를 찾는 모델 세부튜닝
그리드 탐색, 랜덤 탐색
'''
import warnings
warnings.filterwarnings("ignore")

# 기본 입력
import pandas as pd
data = pd.read_csv('07_ML프로세스_2_데이터셋분할과모델검증_vote.csv', encoding='utf-8')

X = data[data.columns[1:13]]
y = data[['vote']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# 1. 그리드 탐색 : 하이퍼파라미터의 특정값을 지정하고, 모델에 적용하며 모델적합도를 비교
from sklearn.model_selection import GridSearchCV
param_grid={'C': [0.001, 0.01, 0.1, 1, 10, 100]}  # 그리드 탐색을 위한 하이퍼 파라미터 설정
from sklearn.linear_model import LogisticRegression

grid_search=GridSearchCV(LogisticRegression(), param_grid, cv=5, return_train_score=True)  # cv : 교차검증 / 훈련 데이터 정확도 제시하기
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
print(grid_search.best_score_)

# 2. 랜덤 탐색 : 하이퍼 파라미터의 지정 없이, 범위를 정하고 그 안에서 무작위로 C 값을 정함


'''
이 다음이 없지 않나?
'''
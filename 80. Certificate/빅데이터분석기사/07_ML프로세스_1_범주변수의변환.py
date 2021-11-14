'''
원 핫 인코딩 : 범주는 크고 작다가 아니라 식별자의 역할을 하므로 더미변수(0, 1)로 변경해야한다.
a : 1, 2 -> a : 0 , 1
b : 1, 2, 3 -> b_1 : 0,1, b_2 : 0,1, b_3 : 0, 1 로 분리
이걸 pd.get_dummies()가 해줌
'''
 
import pandas as pd
data = pd.read_csv('07_ML프로세스_1_범주변수의변환_vote.csv', encoding='utf-8')

X1 = data[['gender', 'region']]
XY = data[data.columns[2:]]
# print(XY)

# get_dummies 이용 전, 성별, 출신지역을 숫자-> 문자표기로 변경 / 이 방식 경고 왜케 많음???
def change_gender(x):
    if x == 1:
        return 'male'
    else:
        return 'female'
X1['gender'] = X1['gender'].apply(change_gender)
# X1['gender'] = X1['gender'].replace([1,2], ['male', 'female'])

X1['region'] = X1['region'].replace([1,2,3,4,5], ['Sudo', 'Chungcheung', 'Honam', 'Youngnam', 'Others']) # 이 방식 경고 있음.(deprecated 직전, pandas의 데이터 일괄 변경 참조)
#print(X1)

# get_dummies 적용
X1_dummy = pd.get_dummies(X1)
#print(X1_dummy)

# 분리한 자료와 다시 통합 하고 저장(괄호 잘 치고, axis=1 빼먹지 말자!)
data = pd.concat([X1_dummy, XY], axis=1)
#print(data)

data.to_csv('07_ML프로세스_2_데이터셋분할과모델검증_vote.csv')
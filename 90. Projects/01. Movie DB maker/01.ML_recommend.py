'''
빅데이터 머신러닝 프로세스를 이용한 영화 추천 시스템
메인 - 인구통계학적 필터링(Demographic Filtering) : 더 인기 있고 비평가들의 찬사를 받은 영화가 일반 관객에게 더 좋아질 확률이 더 높다.
영화별 추천
유저수가 적기 때문에, 콜드 스타트, 계산 효율 저하, 기아 현상이 발생하기 쉽기 때문에
유저의 정보를 기반으로 한 협력 필터링(Collaborative filtering)이 아닌 
영화의 정보를 기반으로 한 컨텐츠 기반 필터링(content based filtering)을 사용
줄거리 설명 기반 추천 : 줄거리 설명을 기반으로 모든 영화에 대한 각각의 유사성 점수를 계산하고 유사성 점수를 기반으로 영화를 추천합니다.
TF-IDF(Term Frequency-Inverse Document Frequency) 벡터를 사용하여 나온 단어의 수가 아닌 빈도를 사용
유사성 점수를 계산하는 데에는 계산이 빠르고 상대적으로 단순한 코사인 유사도 점수를 사용하였습니다.
벡터라이저 된 숫자를 내적하는 것으로 간단하게 구할 수 있습니다.
유사성 점수가 높은 영화를 추천합니다.

레퍼런스 : https://www.kaggle.com/ibtesama/getting-started-with-a-movie-recommendation-system
'''
import pandas as pd 
# import numpy as np 
# Import Tf*IdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer  # 핵심 모델 TF-IDF 벡터라이저 라이브러리 
from sklearn.metrics.pairwise import linear_kernel  # 선형 회귀
import json
from datetime import datetime, timedelta, date

# 00.movie_api에서 만든 기본 json(en) 경로 설정
json_path = "tmdb.json"

# contents에 json 파일 적재
with open(json_path,'r') as j:
    contents=json.loads(j.read())

# tmdb.json에서 최초로 movie 관련 내용이 나오는 json의 인덱스 번호
main_index = next((index for (index, item) in enumerate(contents) if item['model'] == 'movies.movie'), None)

# TF-IDF 벡터라이저 알고리즘에는 영어로 된 overview를 사용하기 때문에,
# 작업에 필요한 pk, original_title, title, overview와 movie_reference_overview만 분류해서 데이터프레임화
pk = []
overview = []
title = []
release_date = []
movie_reference_overview = []

# 메인 알고리즘과 TF-IDF 벡터라이저 알고리즘 양쪽에 사용됨
vote_average = []
vote_count = []
# TF-IDF 벡터라이저 알고리즘용 코사인 유사도 적재 리스트
score = []

# content의 movie 부분을 적재.
for i in range(main_index, len(contents)):
    pk.append(contents[i]["pk"])
    overview.append(contents[i]['fields']["overview"])
    title.append(contents[i]['fields']["title"])
    release_date.append(contents[i]['fields']['release_date'])
    movie_reference_overview.append([])
    vote_count.append(contents[i]['fields']["vote_count"])
    vote_average.append(contents[i]['fields']["vote_average"])
    score.append([])

movie_df = pd.DataFrame({"pk":pk,
                    "title":title,
                    'release_date':release_date,
                    "overview":overview,
                    "movie_reference_overview":movie_reference_overview,
                    "vote_count":vote_count,
                    "vote_average":vote_average,
                    "score":score,
                    })

# 최근 1년간의 영화 데이터만 추출하여 별도로 정의
movie_1y_df = movie_df[movie_df['release_date'] >= (date.today() - timedelta(days=180)).strftime('%Y-%m-%d')]

'''
유사한 영화 5개 받아오는 함수 정의.
'''
# TF-IDF(Term Frequency-Inverse Document Frequency) 벡터라이저 모델을 사용하여 단어의 수를 빈도를 변경
tfidf = TfidfVectorizer(stop_words='english')  # the나 a 등의 조사를 stop_word로 설정하고 지우기 
movie_df['overview'] = movie_df['overview'].fillna('')  # overview 없으면 빈 문자열로 채우고
tfidf_matrix = tfidf.fit_transform(movie_df['overview'])  # 코사인 유사도 계산을 위해 TF-IDF 행렬화

# 내적으로 코사인 유사도 계산
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 영화 이름 입력시 인덱스를 식별하는 메커니즘이 필요하므로 영화 제목과 DataFrame 인덱스간의 역매핑 (이 때 이름 중복 제거)
indices = pd.Series(movie_df.index, index = movie_df['title']).drop_duplicates() 


# 제목을 입력 받아 가장 유사한 10개의 영화목록을 출력하는 함수를 정의
# 타이틀을 넣어주면 연관영화 5개 뽑아오는 함수. 타이틀 반환도 가능하나 여기선 영화 고유 pk반환.
def get_recommendations(title, cosine_sim = cosine_sim):
    idx = indices[title]  # 이름으로 인덱스 긁어오기
    sim_scores = list(enumerate(cosine_sim[idx]))  # 그 영화와 관련된 문자열 코사인 유사성 다 긁어오기
    try:
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # 코사인 유사성 순으로 정렬
    except:
        # 이상치 1등의 이상치를 확인하기 위한 코드
        # print(title+' error')
        pass

    sim_scores = sim_scores[1:6]  # 본인 제외 상위 5개 슬라이스
    movie_indices = [i[0] for i in sim_scores]  # 이름 상태인 영화정보를 인덱스로 역매핑
    # 추천 영화가 5개 미만일 경우, 인구통계학적 필터링(Demographic Filtering)를 기반으로 한 영화 추천
    if len(movie_indices) < 5:
        # print(title+' 5>')  # 이상치 확인 코드
        movie_indices = [75, 34, 13, 0, 42]  # 결과보고 명작 인덱스 역으로 하드 코딩

    # Object 결과를 리스트로 변환하여 반환
    return movie_df['pk'].iloc[movie_indices].values.tolist()  
    


# 반복문으로 데이터 프레임의 'movie_reference_overview' 채우기
# 메인(홈)화면에 사용할 인구통계학적 필터링(Demographic Filtering)를 기반으로 한 영화 추천
answers = []
idx = 0
for title in movie_df['title']:
    # 추천 영화 다섯개를 리스트로 받음
    answers_list = get_recommendations(title)
    if len(answers_list) == 5:
        movie_df.at[idx, 'movie_reference_overview'] = answers_list
        idx += 1
    else: 
        # 있어서는 안되는 종류의 에러
        print('심각한 에러가 발생했습니다.')


'''
메인에 쓸 인구통계학적 필터링 결과 값
'''
# 기본 기준값 : 평점 평균과 투표 수 상위 90%
mm = movie_1y_df['vote_average'].mean()
mc = movie_1y_df['vote_count'].quantile(0.9)
# 조건을 만족하는 영화들을 데이터 프레임으로 정의
movie_score_df = movie_1y_df.loc[movie_1y_df['vote_count'] >= mc].copy()

# 접근 사고 방식 : 3명이 투표한 평점 7.9 영화보다 41명이 투표한 평점 7.6 영화가 더 좋은 영화이다.
def weighted_rating(x, mc=mc, mm=mm):
    v = x['vote_count']
    R = x['vote_average']
    # IMDB 영화 사이트에서 공개한 기본 추천 수식을 채용
    return (v/(v+mc) * R) + (mc/(mc+v) * mm)

# 위 WR 계산 공식을 전용한 score 열을 생성하여 저장
movie_score_df['score'] = movie_score_df.apply(weighted_rating, axis=1)
#movie_df['score'] = movie_df.apply(weighted_rating, axis=1)

# score가 높은 12개의 영화가 선정됨
# 12개를 못뽑는 경우가 발생할 경우 791373, 337404, 508442, 615457, 588228, 527774, 508943, 399566, 438631, 436969, 566525, 423108를 추가한다.
answer = movie_score_df.sort_values('score', ascending=False).head(12)
# 인구 통계학적 결과물! 이걸 직접 필요한 views 함수에 넣는다.
print(answer)

'''
출력 (최종결과물 : tmdb2.json)
'''
with open(json_path,'r') as j:
    json2=json.loads(j.read())

with open("tmdbkr.json",'r') as k:
    jsonkr=json.loads(k.read())

# movie_reference_overview 시리즈에서 원하는 영화 인덱스 데이터와 매칭 시키기 위한 지표
idx2 = 0

#pk 칼럼의 모든 고유넘버에 대해 반복 시행&저장
for p in movie_df['pk']:
    #idx : pk값이 p(pk 칼럼에서 하나하나 뽑아온)인 json2(tmdb의 카피본)에서 해당 pk와 일치하는 영화의 데이터가 들어있는 인덱스 값.
    idx = next((index for (index, item) in enumerate(json2) if item['model'] == 'movies.movie' and item['pk'] == p), None)
    json2[idx]['fields']['movie_reference_overview'] = movie_df[movie_df['pk']==p].movie_reference_overview[idx2]
    #json2[idx]['fields']['score'] = movie_df[movie_df['pk']==p].score[idx2]
    
    json2[idx]['fields']['title'] = jsonkr[idx2]['fields']['title']
    json2[idx]['fields']['overview'] = jsonkr[idx2]['fields']['overview']

    idx2 += 1
    
    
#데이터 프레임 movie_df의 movie_reference_overview json2에 이식&저장완료
with open('tmdb2.json', 'w') as f:
    json.dump(json2, f, indent=4)

with open("tmdb2.json",'r') as t:
    check=json.loads(t.read())
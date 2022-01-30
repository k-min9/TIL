from flask import Flask, jsonify
# ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# 환경변수
import os
from dotenv import load_dotenv
# json to dictionary
import json
# sklearn 머신러닝 라이브러리
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__) 


'''
DB 관련 설정 + ENV 샘플 동봉, 원래는 gitgnore
'''
# Declare connection
# mysql_url = "mysql+pymysql://root:1234@localhost:3306/turtletube_test?charset=utf8"
load_dotenv()
mysql_url = "mysql+pymysql://" + os.environ.get('DB_USER') + ":"+ os.environ.get('DB_PASS') + "@" + os.environ.get('DB_URL') +"?charset=utf8"
engine = create_engine(mysql_url, echo=True, convert_unicode=True)
# Declare & create Session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Create SqlAlchemy Base Instance
Base = declarative_base()
Base.query = db_session.query_property()

def init_database():
    Base.metadata.create_all(bind=engine)

'''
DB 시작/ 종료 설정
'''
@app.before_first_request
def beforeFirstRequest():
    init_database()

@app.teardown_appcontext
def teardownContext(exception):
    db_session.remove()

'''
DTO(Model 아님!) 설정 
'''
class Playlist(Base):
    __tablename__ = 'playlist'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    youtube_tag = Column(String)

'''
실제 작업
'''
# 해당 유저의 정보 확인, 리스트 반환
@app.route("/db/<tid>")
def db_conn(tid):
    # 대분류(type)별 전처리
    # 원래는 여기서 대분류나 타입 분류 (Spring 맞춰서 유저 번호 1번 세팅 해둠)
    playlists = Playlist.query.filter(Playlist.user_id == 1)[:999]  
    playlists_list = list()
    playlists_num = list()
    for idx, playlist in enumerate(playlists):
        tmp_dict = json.loads(playlist.youtube_tag)
        playlists_list.append(tmp_dict)
        playlists_num.append(playlist.id)
        # 나의 번호 기록
        if playlist.id == int(tid):
            request_num = idx

    # 데이터 분석
    vectorizer = DictVectorizer(sparse=False)
    playlists_v = vectorizer.fit_transform(playlists_list)
    cos_sim = cosine_similarity(playlists_v, playlists_v)
    # 해당 유저 내의 순위, 본인 제외 정렬,
    sim_scores = list(enumerate(cos_sim[request_num]))  
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  # 코사인 유사성 순으로 정렬
    sim_scores = sim_scores[1:6]  # 본인 제외 최대 상위 5개 슬라이스 (원래는 O(N)으로 직접 제거하는게 가장 좋음)
    ranking = [i[0] for i in sim_scores]  # 우선 순위
    # 차후 작업
    # if len(ranking) < 5:
    #     ranking = [75, 34, 13, 0, 42]  # 기본 추천 플레이리스트 하드코딩
    # 결과 적재 후 반환
    response = list()
    print('rank', ranking)
    for rank in ranking:
        response.append(playlists_num[rank])

    return jsonify(response)

@app.route("/") 
def hello():
    return "Hello World!"

if __name__ == "__main__" :
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='0.0.0.0')


from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

app = Flask(__name__) 


'''
DB 관련 설정
'''
# Declare connection
mysql_url = "mysql+pymysql://root:1234@localhost:3306/turtletube_test?charset=utf8"
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
class User(Base):
    __tablename__ = 'user'

    user_seq = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(String)

'''
실제 작업
'''
# 해당 유저의 정보 확인, 리스트 반환
@app.route("/db/<tid>")
def db_conn(tid):
    user = User.query.filter(User.user_seq == tid).first()
    print(user.email)

    res = [1, 2, 3]
    res.append(user.email)
    
    return jsonify(res)

@app.route("/") 
def hello():
    return "Hello World!"

if __name__ == "__main__" :
    # app.run(host='127.0.0.1', port=8080, debug=True)
    app.run(host='0.0.0.0')


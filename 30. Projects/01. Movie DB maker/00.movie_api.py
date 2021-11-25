import requests
import json
from datetime import date


# API 신청용 URL 조합용 클래스
class URLMaker:
    #api 기본 주소세팅. 뒤에 쿼리 덧붙여서 명령별 구별 
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    # 영화/추천영화 한 페이지 긁어오기(ML용)
    # GET movie/popular (https://developers.themoviedb.org/3/movies/get-popular-movies)
    def get_movie_url(self, category='movie', feature='popular', page='1'):
        #위의 url(자기자신 소속 url 데이터 line 6)/movie/popular 로 기능 구동
        url = f'{self.url}/{category}/{feature}'
        #뒤에 쿼리로 인증용 필수 데이터 api_key(line 8), 옵션 데이터인 언어(한글-한국), 페이지수(1페이지) 덧붙임
        url += f'?api_key={self.key}&language=en-US&page={str(page)}'

        #그렇게 만든 최종 명령 url 반환
        return url
    
    # 영화/추천영화 한 페이지 긁어오기(한글판)
    def get_movie_url_kr(self, category='movie', feature='popular', page='1'):
        #위의 url(자기자신 소속 url 데이터 line 6)/movie/popular 로 기능 구동
        url = f'{self.url}/{category}/{feature}'
        #뒤에 쿼리로 인증용 필수 데이터 api_key(line 8), 옵션 데이터인 언어(한글-한국), 페이지수(1페이지) 덧붙임
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'

        #그렇게 만든 최종 명령 url 반환
        return url
    
    # 장르 정보 긁어오기 (https://developers.themoviedb.org/3/genres/get-movie-list)
    def get_genre_url(self):
        url = f'{self.url}/genre/movie/list?api_key={self.key}'
        return url


# 인증키
TMDB_KEY = '본인의 키를 넣어주세요!'
# url 조합해주는 클래스 선언
url = URLMaker(TMDB_KEY)
# 1~1000 페이지의 범위를 설정하여 영화를 가져올 수 있음 (상수화하여 kr과 en버전이 상이해지는 경우를 방지)
PAGES = 100

def create_genre_data():
    # line 37에서 반환한 url값 받아와 저장
    genre_url = url.get_genre_url()
    # 리퀘스트 데이터 저장
    raw_data = requests.get(genre_url)
    # 해당 데이터 json화
    json_data = raw_data.json()
    # 시킨것에서 genres라는 키의 밸류값 추출
    genres = json_data.get('genres')

    # 장르 데이터 저장용 빈 리스트 생성. 여기에 딕셔너리 하나씩 넣을 예쩡
    genre_data = []

    # genres의 모든 원소들을 하나하나 tmp에 저장한뒤 genre_data에 하나하나 추가함
    for genre in genres:
        tmp = {
            # 나중에 찾아오려는 심산인지 모델명을 movies.genre로 통일시켜둠
            'model': 'movies.genre',
            'pk': genre['id'],
            'fields': {
                'name': genre['name']
            }
        }
        genre_data.append(tmp)

    # 모든 moives의 movie들을 다 돌려 원하는 내용만 만들어 추가한 딕셔너리 덩어리 genre_data 다 만든 뒤,
    # tmdb.json을 쓰기전용 사양('w')으로 오픈. 없다면 해당 빈파일 생성하고 있다면 싹 비우고 내용입력 시작.    
    with open('tmdb.json', 'w') as f:
        # 파이썬 객체를 json문자열로 변환. 위에 '열어둔' tmdb.json(이하 f)에 genre_data 파일 싹 입력. 
        # indent : 들여쓰기 옵션. 보통 4로 놓고쓰며 줄바꿈 잘 되고 이쁘게 된다.
        # load와 마찬가지로 파이썬 내부에 놓고 쓰려면 dumps쓰면 되는데 잘 쓰진 않는것같다.
        json.dump(genre_data, f, indent=4)

def create_movie_data():
    # 'tmdb.json' 읽어오기. r+는 읽기 또는 쓰기모드. 밑에 w도 있는데 w는 여는순간(없다면 새로 만들어서라도) 안의 내용물 싹 밀어버리고 기록하는 타입이라면
    # r+는 내용물은 건드리지 않고 이어 기록하는 타입. 따라서 수정할거면 무조건 w를 써야하지만 추가만 할거면 r+가 안전하다. 이하 f로 약칭.
    with open('tmdb.json', 'r+') as f:
        # json.load()로 외부의 json파일(여기선 open한 tmdb)을 파이썬 객체화 시킨놈이 movie_data (디코딩)
        # json.loads()도 있는데 이건 쉽게말해서 파이썬 내부 json타입 데이터스트링을 json 오브젝트로 만들때 쓴다고 보면 편하다 (인코딩)
        movie_data = json.load(f)

    current_date = date.today().isoformat()

    for page in range(1, PAGES):
        # 외부 데이터
        raw_data = requests.get(url.get_movie_url_kr(page=page))
        # 외부 데이터 -> 파이썬 딕셔너리로
        json_data = raw_data.json()
        # 그 중에서 필요한 movie 정보
        movies = json_data.get('results')

        #movies의 각 원소들에 대해 그 원소들과 대응하는 데이터 추출. 
        for movie in movies:
            
            # 데이터 전처리
            # release_date, poster_path, backdrop_path등이 비어있는 등 정보가 충분하지 않은 영화나(결측치)
            # 10점, 0점등의 vote_average나, 현재 날짜를 이후의 개봉일자(release_date) (이상치)같은 데이터를 전처리한다.
            if movie.get('release_date') and movie.get('poster_path') and movie.get('backdrop_path') and 0 < movie.get('vote_average') < 10 and current_date >= movie.get('release_date') :
                #.pop() 리스트의 마지막 데이터를 뽑아내고 삭제함. 
                
                # DB에 적재하지 않지만, API에서 내려온 내용은 여기서 삭제한다.
                movie.pop('video')
                movie.pop('original_language')
                movie.pop('adult')

                # 01.recommended에서의 결과값과 과정을 담을 빈 리스트를 추가한다.
                movie['movie_reference_overview'] = []
                #movie['score'] = []

                # loaddata 명령어시, JSON을 DB에 적재할 수 있도록 세팅
                tmp = {
                    'model': 'movies.movie',
                    'pk': movie.pop('id'),
                    'fields': movie,
                }
                # movie_data에 세팅 내용을 추가
                movie_data.append(tmp)

    # 모든 moives의 movie들을 다 돌려 원하는 내용만 만들어 추가한 딕셔너리 덩어리 movie_data 다 만든 뒤,
    # tmdb.json을 쓰기전용 사양('w')으로 오픈. 없다면 해당 빈파일 생성하고 있다면 싹 비우고 내용입력 시작.
    with open('tmdb.json', 'w') as f:
        # 파이썬 객체를 json문자열로 변환. 위에 '열어둔' tmdb.json(이하 f)에 movie_data 파일 싹 입력. 
        # indent : 들여쓰기 옵션. 보통 4로 놓고쓰며 줄바꿈 잘 되고 이쁘게 된다.
        # load와 마찬가지로 파이썬 내부에 놓고 쓰려면 dumps쓰면 되는데 잘 쓰진 않는것같다.
        json.dump(movie_data, f, indent=4)

# 최종적인 JSON의 overview와 title은 한글이어야하기 때문에, tmdbkr을 생성하고 차후 최종 파일에 반영한다.
def create_movie_kr_data():
    movie_data = []
    current_date = date.today().isoformat()

    for page in range(1, PAGES):
        # 외부 데이터
        raw_data = requests.get(url.get_movie_url_kr(page=page))
        # 외부 데이터 -> 파이썬 딕셔너리로
        json_data = raw_data.json()
        # 그 중에서 필요한 movie 정보
        movies = json_data.get('results')
        # json_data의 results 키값을 갖는 밸류값들만 토해서 movies에 저장. 타입:list
        # movies = requests.get(url.get_movie_url_kr(page=page)).json().get('results')

        #movies의 각 원소들에 대해 그 원소들과 대응하는 데이터 추출.
        for movie in movies:
            # 데이터 전처리
            # release_date, poster_path, backdrop_path등이 비어있는 등 정보가 충분하지 않은 영화나(결측치)
            # 10점, 0점등의 vote_average나, 현재 날짜를 이후의 개봉일자(release_date) (이상치)같은 데이터를 전처리한다.
            if movie.get('release_date') and movie.get('poster_path') and movie.get('backdrop_path') and 0 < movie.get('vote_average') < 10 and current_date >= movie.get('release_date') :
                # loaddata 명령어시, JSON을 DB에 적재할 수 있도록 세팅
                tmp = {
                    'model': 'movies.movie',
                    'pk': movie.pop('id'),
                    'fields': movie,
                }
                # movie_data에 세팅 내용을 추가
                movie_data.append(tmp)

    with open('tmdbkr.json', 'w') as f:
        json.dump(movie_data, f, indent=4)


create_genre_data()
create_movie_data()
create_movie_kr_data()



'''
pickle은 파이썬 내장 모듈로 단일 객체를 저장하고 불러올 수 있음
dictionary 등도 가능하고, 파일 형태 등을 신경 쓰지 않다는 점에서 json dump에 비해 편하기도 함
여러 객체를 저장할때는 파일 수가 늘어나고, 객체의 내용 중 하나만 바꿔도 전체 객체를 저장해야하는 점이 단점
'''
import pickle

# 객체를 파일에 저장하는 함수
def save_object(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

# 파일에서 객체를 불러오는 함수
def load_object(filename):
    with open(filename, 'rb') as file:
        obj = pickle.load(file)
        return obj

# 객체를 저장
data_to_save = {"key": "value"}
save_object(data_to_save, 'data.pickle')

# 객체 불러오기
loaded_data = load_object('data.pickle')
print(loaded_data)

import json
import pickle

name = 'meta'

# JSON 파일에서 데이터 읽어오기
json_file_path = name + '.json'
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    
# pickle 파일로 저장
pickle_file_path = name + '.pickle'
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(data, pickle_file)

print(f'Pickle 파일이 성공적으로 생성되었습니다. 경로: {pickle_file_path}')

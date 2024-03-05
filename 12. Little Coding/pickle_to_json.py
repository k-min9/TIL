import json
import pickle

name = 'meta'

# pickle 파일에서 데이터 읽어오기
with open(name+'.pickle', 'rb') as pickle_file:
    data = pickle.load(pickle_file)

# JSON 파일로 저장
json_file_path = name + '.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)

print(f'JSON 파일이 성공적으로 생성되었습니다. 경로: {json_file_path}')

'''
CSV를 읽고 해당 내용 중 필요한 row를 json 안의 list 형태로 변환
'''
import pandas as pd
import json

# CSV 파일 읽기
df = pd.read_csv('datas.csv')

# JSON 형식으로 변환
datas_json = []
for index, row in df.iterrows():
    data = {
        "Identifier": row['Identifier'].strip()+"j",  # id에 j를 붙이는 등의 내용 추가
        "Name": row['Name'].strip(),
        "Nickname": row['Nickname'].strip() if not pd.isna(row['Nickname']) else "",  # 없을 경우 빈 string
        "dataReference": row['dataReference'],
        "OriginalIdentifier": None,
        "SpinePortraitPath": None,
        "SmallPortraitPath": None
    }
    datas_json.append(data)

# JSON 파일로 저장
with open('datas.json', 'w', encoding='utf-8') as json_file:
    json.dump(datas_json, json_file, ensure_ascii=False, indent=2)

print("JSON 파일이 생성되었습니다.")

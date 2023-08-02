import json
import os
import shutil

folder_path = "."
json_file_path = "Catalog.json"  # 외부 JSON 파일 경로

# JSON 파일 읽기
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# JSON 데이터에서 메타데이터와 오디오 파일 매핑
c_filename = dict()
c_path = dict()

for key, value in json_data["Table"].items():
    crc = value["Crc"]
    fileName = value["fileName"]
    path = value["path"]
    path = path.rsplit(fileName, 1)[0]
    
    # 메타데이터와 파일 이름을 매핑하여 딕셔너리에 저장
    c_filename[crc] = fileName
    c_path[crc] = path

    # print(key, crc, fileName)
print(c_path)
# 폴더 내의 파일을 반복하면서 작업 수행
for filename in os.listdir(folder_path):
    if filename.endswith(".dat"):
        # 파일 이름 분리
        parts = filename.split("_")
        if len(parts) == 2:
            a, b = parts
            b = b.split(".")[0]  # 파일 확장자 제거

            print(a,b)

            if int(b) in c_path: # 딕셔너리에 path 등록 여부 확인
                try:
                    newPath = c_path[int(b)]
                    newFilename = c_filename[int(b)]                  

                    source_file = os.path.join(folder_path, a)  # 현재 파일
                    target_folder = os.path.join(folder_path, newPath)  # 이동 폴더
                    if not os.path.exists(target_folder):  # 없을 경우 생성
                        os.makedirs(target_folder)
                    shutil.copy2(source_file, target_folder)  # 복사
                    copy_file = os.path.join(target_folder, a+'.ogg')  # 복사된 파일
                    target_file = os.path.join(target_folder, newFilename)  # 변경 경로 + 바뀔 이름

                    os.rename(source_file, target_file)  # 이름 변경
                except Exception:
                    print('Exception', c_filename[int(b)])


print("파일 분류가 완료되었습니다.")

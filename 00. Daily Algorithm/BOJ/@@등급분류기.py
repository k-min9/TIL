import os
import shutil

source_folder = "./" 
destination_folder = "./등급별/"

# 폴더 생성 함수
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# 원본 폴더 내의 파일들을 검색하고 복사
for entry in os.scandir(source_folder):
    if entry.is_file():
        filename = entry.name
        file_path = entry.path
        print(file_path)
        
        # 파일 이름에서 _로 split하여 두 번째 단어를 얻음
        split_result = filename.split("_")
        if len(split_result) > 1:
            sub_folder_name = split_result[1]
            sub_folder_path = os.path.join(destination_folder, sub_folder_name)
            
            # 스크립트 자체를 복사하지 않도록 예외 처리
            if filename != os.path.basename(__file__):
                create_directory(sub_folder_path)  # 하위 폴더 생성
                
                destination_file_path = os.path.join(sub_folder_path, filename)
                
                shutil.copy(file_path, destination_file_path)  # 파일 복사

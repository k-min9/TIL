'''
실제 배포기능도 포함
'''
import os
import pickle
import urllib.request
import sys
import ctypes
from tqdm import tqdm

# 관리자 권한으로 재 실행
def react_as_admin():
    # 관리자 권한 확인
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
        
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        print("이미 관리자 권한으로 실행중입니다.")


def download_file(url, destination):
    try:
        urllib.request.urlretrieve(url, destination)
    except Exception as e:
        print("다운로드 중 오류 발생:", e)
        response = input("프로그램을 관리자 권한으로 다시 실행하시겠습니까? (y/n): ")
        if response.lower() == 'y':
            react_as_admin()
        else:
            print("관리자 권한이 필요없는 폴더에서 다시 실행해주세요.")
            input("아무 키나 눌러서 종료해주세요...")

def download_with_progress(url, output_file):
    with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
        file_size = int(response.info().get('Content-Length', -1))
        block_size = 1024  

        with tqdm(total=file_size, unit='B', unit_scale=True, desc=output_file, ncols=80) as pbar:
            while True:
                buffer = response.read(block_size)
                if not buffer:
                    break
                out_file.write(buffer)
                pbar.update(len(buffer))

if __name__ == "__main__":
    print('Install.exe start')    
    os.makedirs('config', exist_ok=True)  # config 폴더가 없으면 생성
    
    # meta.pickle 문답무용 다운로드 + 관리자 권한 해결
    print('Get latest metafile...') 
    file_url = 'https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/config/meta.pickle?download=true'
    file_destination = "./config/meta.pickle"
    download_file(file_url, file_destination)
    
    meta_version_eden = 0
    meta_version_setting = 0
    meta_version_eden_name = ''  # 보이는 이름
    meta_version_setting_name = ''
    try:
        with open('config/meta.pickle', 'rb') as file:
            settings_eden = pickle.load(file)
            if 'meta_version_eden' in settings_eden:
                meta_version_eden = settings_eden['meta_version_eden']
            if 'meta_version_setting' in settings_eden:
                meta_version_setting = settings_eden['meta_version_setting']
            if 'meta_version_eden_name' in settings_eden:
                meta_version_eden_name = settings_eden['meta_version_eden_name']
            if 'meta_version_setting_name' in settings_eden:
                meta_version_setting_name = settings_eden['meta_version_setting_name']
    except:
        print('meta 정보에 문제가 있습니다. 신고해주시면 대응하겠습니다.')
    
    #### eden.pickle 로딩
    version_eden = ''
    data = dict()
    if os.path.exists("./config/eden.pickle"):
        try:
            with open('./config/eden.pickle', 'rb') as file:
                data = pickle.load(file)
                if 'version' in data:
                    version_eden = data['version']
        except:
            print('eden 정보에 문제가 있습니다. 신고해주시면 대응하겠습니다.')
    
    if version_eden == meta_version_eden:
        print('eden은 최신버전입니다.')
    else:
        print('Downloading eden.exe')
        # eden 파일 받음 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # download_with_progress('https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/eden.exe?download=true', 'eden.exe')
        # download_with_progress('https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/main.exe?download=true', 'main.exe')

        # eden 버전 갱신
        data['version'] = meta_version_eden
        data['version_name'] = meta_version_eden_name
            
    with open('./config/eden.pickle', 'wb') as file:
        pickle.dump(data, file)
        
    #### setting.pickle 로딩
    version_setting = ''
    data = dict()
    if os.path.exists("./config/setting.pickle"):
        try:
            with open('./config/setting.pickle', 'rb') as file:
                data = pickle.load(file)
                if 'version' in data:
                    version_setting = data['version']
        except:
            print('setting 정보에 문제가 있습니다. 신고해주시면 대응하겠습니다.')
    
    if version_setting == meta_version_setting:
        print('arona.exe은 최신버전입니다.')
    else:
        print('Downloading arona.exe')
        # setting 파일 받음
        download_with_progress('https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/arona.exe?download=true', 'main.exe')
        # download_with_progress('https://huggingface.co/mingu4969/windows-archive-dist/resolve/main/main.exe?download=true', 'main.exe')

        # setting 버전 갱신
        data['version'] = meta_version_setting
        data['version_name'] = meta_version_setting_name
            
    with open('./config/setting.pickle', 'wb') as file:
        pickle.dump(data, file)
        
    print('version eden', version_eden)    
    input('모든 작업이 종료 되었습니다. 아무 키나 눌러서 종료해주세요.')

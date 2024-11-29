'''
pip install supabase

기본 무료인 오픈소스 supabase에 json 업로드/다운로드하기

1. project 만들고 url, key 복사 SUPABASE_URL, SUPABASE_KEY에 붙여넣기 (KEY는 별도 발급도 가능)
2. 좌측 storage에서 public으로 new bucket 만들고, bucket_name으로 활용
3. policy는 For Full Custom하고 CRUD 풀 오픈
'''
import json
from supabase import create_client, Client

# Supabase 프로젝트 URL과 API Key 설정 (공개되도 되는 Free API KEY)
SUPABASE_URL = "https://xxxxx.supabase.co"
SUPABASE_KEY = "key here!"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#  URL을 받아 JSON 파일로 저장한 후 Supabase 스토리지에 업로드
def post_ngrok_path(url: str):
    file_name = "my_little_jarvis_plus_ngrok_server.json"
    bucket_name = "json_bucket"

    # JSON 데이터를 파일로 저장
    json_data = {"url": url}
    local_file_path = f"./{file_name}"

    with open(local_file_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    # Supabase 스토리지에 파일 업로드
    with open(local_file_path, "rb") as f:
        response = supabase.storage.from_(bucket_name).upload(
            file=f,
            path=file_name,
            file_options={"cache-control": "3600", "upsert": "true"},  # 파일 덮어쓰기 설정
        )

    if isinstance(response, dict) and response.get("error"):
        print("Error uploading file:", response["error"])
    else:
        print(f"File {file_name} successfully uploaded or updated.")

#  Supabase에서 JSON 파일을 다운로드하고 내용을 출력
def get_ngrok_path():
    file_name = "my_little_jarvis_plus_ngrok_server.json"
    bucket_name = "json_bucket"
    local_file_path = f"./{file_name}"

    # Supabase 스토리지에서 파일 다운로드
    response = supabase.storage.from_(bucket_name).download(file_name)

    if isinstance(response, dict) and response.get("error"):
        print("Error downloading file:", response["error"])
    else:
        # 다운로드된 내용을 로컬 파일에 저장
        with open(local_file_path, "wb") as f:
            f.write(response)

        # 저장된 파일을 읽어 JSON 데이터 파싱 및 출력
        with open(local_file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
            print(json_data)

if __name__ == "__main__":
    # 테스트용 업로드 및 다운로드 호출
    post_ngrok_path("https://test-url.com")
    get_ngrok_path()

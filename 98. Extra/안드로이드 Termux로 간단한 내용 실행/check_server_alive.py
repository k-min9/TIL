import sys
import requests
from config import JSON_URL, SUPABASE_API_KEY, TARGET_SERVER_ID


def get_server_url(server_id: str) -> str | None:
    headers = {"Authorization": f"Bearer {SUPABASE_API_KEY}"}
    
    try:
        resp = requests.get(JSON_URL, headers=headers, timeout=10)
        resp.raise_for_status()
        full_data = resp.json()
    except Exception as e:
        print(f"❌ 요청 실패: {e}")
        return None

    if server_id not in full_data:
        print(f"❌ 서버 ID '{server_id}' 없음")
        return None

    data = full_data[server_id]
    url = data.get("url")
    status = data.get("status")
    
    if status != "open":
        print(f"⚠️  Server {status}")
        return None

    return url


def check_alive(base_url: str) -> bool:
    alive_url = f"{base_url.rstrip('/')}/alive"
    
    try:
        resp = requests.get(alive_url, timeout=5)
        return resp.status_code == 200
    except:
        return False


def main():
    print(f"🔍 {TARGET_SERVER_ID} 체크 중...\n")
    
    url = get_server_url(TARGET_SERVER_ID)
    if not url:
        print("❌ 서버 사용 불가")
        sys.exit(1)
    
    if check_alive(url):
        print(f"✅ {TARGET_SERVER_ID} 정상")
        sys.exit(0)
    else:
        print(f"❌ {TARGET_SERVER_ID} 다운")
        sys.exit(1)


if __name__ == "__main__":
    main()
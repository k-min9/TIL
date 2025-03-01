import requests
import time
import hashlib
import hmac
import base64

# SwitchBot API 정보
TOKEN = "YOUR_OPEN_TOKEN"  # 발급받은 Open Token
SECRET = "YOUR_SECRET_KEY"  # 발급받은 Secret Key
API_URL = "https://api.switch-bot.com/v1.1/devices"

# 요청에 필요한 헤더 생성 함수
def generate_headers():
    t = str(int(time.time() * 1000))  # 현재 timestamp (밀리초)
    nonce = ""  # nonce는 비워도 됨
    
    # Sign 생성 (HMAC-SHA256 방식)
    string_to_sign = f"{TOKEN}{t}{nonce}"
    sign = base64.b64encode(
        hmac.new(SECRET.encode(), string_to_sign.encode(), hashlib.sha256).digest()
    ).decode()

    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json",
        "t": t,
        "sign": sign,
        "nonce": nonce,
    }
    return headers

# 디바이스 목록 요청 함수
def get_device_list():
    headers = generate_headers()
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # JSON 응답 반환
    else:
        return {"error": response.status_code, "message": response.text}

# 실행 예제
if __name__ == "__main__":
    device_list = get_device_list()
    print(device_list)

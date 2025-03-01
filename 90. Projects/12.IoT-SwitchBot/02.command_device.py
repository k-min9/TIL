import requests
import time
import hashlib
import hmac
import base64

# SwitchBot API 정보
TOKEN = "YOUR_OPEN_TOKEN"  # 발급받은 Open Token
SECRET = "YOUR_SECRET_KEY"  # 발급받은 Secret Key
BASE_URL = "https://api.switch-bot.com/v1.1"

# 제어할 디바이스 ID (봇 1)
DEVICE_ID = "DEVICE_ID"

# 요청 헤더 생성 함수
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

# 디바이스 제어 함수
def send_command(device_id, command):
    url = f"{BASE_URL}/devices/{device_id}/commands"
    headers = generate_headers()
    data = {
        "command": command,
        "parameter": "default",
        "commandType": "command"
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()  # JSON 응답 반환
    else:
        return {"error": response.status_code, "message": response.text}

# 봇 제어 함수
def turn_on_bot():
    return send_command(DEVICE_ID, "turnOn")

def turn_off_bot():
    return send_command(DEVICE_ID, "turnOff")

def press_bot():
    return send_command(DEVICE_ID, "press")

# 실행 예제
if __name__ == "__main__":
    print("Turning on bot...")
    print(turn_on_bot())

    # print("Turning off bot...")
    # print(turn_off_bot())

    # print("Pressing bot...")
    # print(press_bot())

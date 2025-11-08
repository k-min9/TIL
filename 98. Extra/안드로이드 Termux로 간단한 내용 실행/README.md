# 개요

- 단순한 서버 상태 확인 작업은 Termux라는 툴로 간단한 스크립트를 작성해 수행할 수 있음
- Termux는 안드로이드 환경에서 Linux 명령어와 Python을 실행할 수 있는 터미널 앱임
- Supabase Storage에 저장된 JSON을 읽어와, 각 서버의 `/alive` 상태를 확인하는 간단한 스크립트를 실행함
- 별도 앱 개발 없이, Termux에서 명령어 한 줄로 서버 상태를 확인하는 것을 목표로 함

## 설치

### 1. Termux 설치

- Google Play Store에서 `Termux` 설치

### 2. Python 환경 구성

```bash
pkg update
pkg install python
pip install requests
```

### 3. 스크립트 작성

- `config.py` 작성 (URL, API KEY, TARGET_SERVER_ID 설정)
- `check_server_alive.py` 작성 (메인 로직)

### 4. 파일 구조에 맞게 넣기

최상단의 Termux 폴더 만들고 코드 복사

```markdown
~/termux/
├── check_server_alive.py    # 메인 스크립트
├── config.py                 # 설정 파일
```

### 5. 실행 권한 부여

```bash
termux-setup-storage  # 공유저장서 접근설정
chmod +x ~/storage/shared/termux/check_server_alive.py
python ~/storage/shared/termux/check_server_alive.py
```

### 5-1. 간단명령어로 실행하게 세팅

```bash
echo "alias cs='python ~/storage/shared/termux/check_server_alive.py'" >> ~/.bashrc
source ~/.bashrc
```

## 사용 방법

### 터미널에서 직접 실행

```bash
python ~/storage/shared/termux/check_server_alive.py
```
  
or  
  
```bash
cs  # 간단명령어 세팅시
```

### 설정 변경

- 다른 서버 체크: `config.py`의 `TARGET_SERVER_ID` 값만 변경
- URL/API 키 변경: `config.py`의 `JSON_URL`, `SUPABASE_API_KEY` 수정

# ✅ Asset Downloader 사용을 위한 작업 기록

## 0. 개요

이 문서는 **BA-AD (Blue Archive - Asset Downloader)** 관련 프로젝트들을 활용하여  
**게임 Asset 다운로드 및 추출** 작업을 수행한 과정을 복기하고, 향후 동일한 작업을 반복할 수 있도록 정리.

### 🎯 작업 목표

- 게임 서버로부터 리소스 파일 (예: AssetBundle 등)을 다운로드
- 다운로드된 리소스를 해석하여 실제 에셋 (텍스처, 오디오 등)으로 추출

### ⚙️ 사용한 GitHub 프로젝트 및 역할 분담

| 프로젝트 명칭 | GitHub 주소 | 역할 | 비고 |
|---------------|-------------|------|------|
| **BA-AD (다운로드 프로젝트)** | [`Deathemonic/BA-AD`](https://github.com/Deathemonic/BA-AD) | **게임 리소스 다운로드** |  |
| **BA-AD-Extract (추출 프로젝트)** | [`Sunset-Edu-Tech-Group/BA-AD`](https://github.com/Sunset-Edu-Tech-Group/BA-AD/tree/main) | **다운로드된 리소스 추출** | 다운로드 기능 오류 |

> 이하 문서에서는 각각을 **다운로드 프로젝트**와 **추출 프로젝트**로 명시하여 구분합니다.

## 1. 환경설정

1. 다운로드 프로젝트에서 Releases로 가서 최신 baad 파일(윈도우 버전)으로 다운로드  
2. 추출 프로젝트는 `git clone`하고 해당 폴더로 이동하여서, `uv venv` 후, `uv pip install .`  

## 2. 실행

1. 다운로드 프로젝트 폴더로 이동하여 PowerShell을 통해 `.\baad.exe download japan` 로 실행  
2. output 폴더에 다운로드 된 파일들을 폴더째 추출 프로젝트로 붙여넣기  
3. VS Code 등을 열고, `source .venv/Scripts/activate` 로 가상환경 활성화  
4. `baad download --media` 로 실행. `output/MediaExtracted` 폴더 내용물 확인  
5. 종료

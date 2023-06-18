# 배포 환경 정보 설정 tf파일
provider "google" {
  credentials = file("../credentials/PROJECT.json")  # GCP 프로젝트의 인증 정보가 포함된 JSON 파일의 경로입니다.

  project = "PROJECT"  # Terraform에서 관리할 GCP 프로젝트의 ID입니다.
  region = "asia-northeast3"  # 리소스를 배포할 GCP 리전입니다.
  zone = "asia-northeast3-a"  # 리소스를 배포할 GCP 존입니다.
}

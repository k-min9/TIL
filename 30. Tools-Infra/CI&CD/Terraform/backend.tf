# Terraform으로 구성한 인프라 상태 파일(Terraform state)을 저장하기 위한 백엔드(backend) 설정
terraform {
  backend "gcs" {
    credentials = "../credentials/PROJECT.json"  # GCS(Google Cloud Storage)에 액세스하기 위한 인증 정보가 포함된 JSON 파일의 경로입니다.
    bucket = "PROJECT-bucket"  # Infra 상태 파일을 저장할 GCS 버킷의 이름입니다.
    prefix = "jenkins.terraform.tfstate"  # 저장된 상태 파일의 경로와 이름을 지정합니다.
  }
}

# Terraform에서 사용할 Provider와 Terraform 버전을 지정하는 설정 파일
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"  # 사용할 Google Cloud Platform (GCP) Provider의 소스 경로입니다.
      version = "~> 4.0"  # GCP Provider의 버전 제한을 설정합니다. "~> 4.0"은 4.x.x 버전 범위 내에서 가장 최신 버전을 사용하도록 지정합니다.
    }
    google-beta = {
      source = "hashicorp/google-beta"  # 사용할 Google Cloud Platform (GCP) Beta Provider의 소스 경로입니다.
      version = "4.27.0"  # GCP Beta Provider의 버전을 4.27.0으로 고정합니다.
    }
  }

  required_version = "~> 1.0"  # Terraform의 최소 버전 제한을 설정합니다. "~> 1.0"은 1.x.x 버전 범위 내에서 가장 최신 버전을 사용하도록 지정합니다.
}

# jenkins가 들어간 machine image를 이용하여 서버 설정
resource "google_compute_instance_from_machine_image" "jenkins-instance" {
  provider = google-beta  # google-beta Provider를 사용하여 리소스를 관리합니다.
  name = "jenkins-vm-instance"  # 생성할 인스턴스의 이름입니다.
  zone = "asia-northeast3-a"  # 인스턴스가 속할 GCP 리전의 존을 지정합니다.

  source_machine_image = "projects/machineImages/jenkins"  # 사용할 Jenkins를 포함한 머신 이미지의 경로를 지정합니다.

  network_interface {
    subnetwork = google_compute_subnetwork.public-subnet.self_link  # 인스턴스가 속할 서브넷의 self_link를 참조합니다.
    access_config {
      # 공란시 일회용 IP(Ephemeral IP) 사용
    }
  }

  metadata_startup_script = file("init/init.sh")  # 인스턴스 시작 시 실행될 스크립트 파일의 경로를 지정합니다.

  service_account {
    email = "email@email.com"  # 인스턴스에 할당할 서비스 계정의 이메일 주소를 지정합니다.
    scopes = ["cloud-platform"]  # 서비스 계정의 스코프를 "cloud-platform"으로 설정합니다.
  }
}

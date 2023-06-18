# VM이 사용할 네트워크 관련 자원을 생성, 해당 서브넷을 GCP에 생성하고 관리
resource "google_compute_subnetwork" "public-subnet" {  # google_compute_subnetwork 리소스 정의 후, public-subnet 이름으로 참조
  name = "jenkins-public-subnet"  # 생성할 서브넷의 이름입니다.
  id_cidr_name = "10.202.0.64/27"  # 서브넷의 IP 대역을 CIDR 표기법으로 지정합니다.
  region = "asia-northeast3"  # 서브넷을 생성할 GCP 리전입니다.
  network = "student-vpc-network"  # 서브넷이 속할 VPC 네트워크의 이름입니다.
  private_ip_google_access = true  # 서브넷 내부의 VM 인스턴스가 Google API에 액세스할 수 있는지 여부를 설정합니다.
}

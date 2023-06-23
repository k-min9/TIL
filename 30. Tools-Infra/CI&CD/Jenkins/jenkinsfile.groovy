#!groovy
env.submitter = ''
env.projectid = ''

pipeline {
  agent any // Jenkins 마스터 노드 또는 연결된 슬레이브 노드 중에서 파이프라인을 실행할 수 있는 모든 노드에서 작업을 수행

  stages {
    // 초기화 단계
    stage("Initialize") {
      steps {
        script {
          // 현재 프로젝트 ID 가져오기
          env.projectid = sh(script: 'gcloud config get-value project', returnStdout: true).trim()
          echo env.projectid
          
          // 서비스 계정 인증 및 초기화 스크립트 실행
          sh("gcloud auth activate-service-account --key-file=/credentials/${env.projectid}.json")
          sh("./init.sh")
          
          // kubectl.yml 파일에서 _BRANCH_NAME_을 "sample"으로 치환
          sh("sed -i -e s/_BRANCH_NAME_/sample/g kubectl.yml")
        }
      }
    }

    // 애플리케이션 빌드 단계
    stage("App Build") {
      steps {
        script {
          println("***App Build***")
          sh("./gradlew build")
        }
      }
    }

    // 도커 이미지 빌드 및 푸시 단계
    stage("Docker Build & Push") {
      steps {
        script {
          println("***Docker Build & Push***")
          
          // 도커 이미지 빌드
          sh("docker build -t asia.gcr.io/${env.projectid}/sample:1.0")
          
          // gcloud 도커 인증 구성 및 이미지 푸시
          sh("echo 'Y' | gcloud auth configure-docker")
          sh("docker push asia.gcr.io/${env.projectid}/sample:1.0")
        }
      }
    }

    // 인프라 체크 단계
    stage("Infra check") {
      steps {
        // InfraDeployLock 락을 사용하여 동시에 인프라 체크 수행 제한
        lock('InfraDeployLock') {
          script {
            println("***Infra check***")
            
            // 인프라 코드 디렉토리로 이동 및 Terraform 초기화 및 적용
            sh("""
                ch ./iac/cicd-cluster
                terraform init -backend-config="prefix=prod" -no-color
                terraform apply -var-file="configurations/prod-config.tfvars" -auto-approve -no-color
                gcloud container clusters list
            """)
          }
        }
      }
    }

    // Kubernetes 배포 단계
    stage("Kubernetes Deploy") {
      steps {
        script {
          println("***Kubernetes Deploy***")
          
          // cicd-cluster의 인증 정보를 가져와서 kubectl 설정
          sh("gcloud container clusters get-credentials cicd-cluster --zone asia-northeast3-a --project ${env.projectid}")
          
          // kubectl.yml 파일을 사용하여 Kubernetes 리소스 배포
          sh("kubectl apply -f kubectl.yml")    
        }
      }
    }
  }
}

# 운영 체제론 (Operating System)

정의 : 사용자에게 프로그램을 쓰기 쉽고, 효율적이고 빠르게 사용할 수 있는 환경을 제공
역할 : (물리 하드웨어) 가상화, 리소스 관리

## Limited Direct Execution

정의 : CPU의 직접 제어  

Dual mode = User mode + Kernel mode

- Interupt vs trap
  - interrupt : 현재 실행 프로그램과 상관 없이 프로그램을 중지(SW, HW 구분없음)
  - trap : SW가 만들어낸 interrupt
    - exception (ex - 0으로 나눴을때)
    - system call (user 프로그램으로부터 system에 요청)

context switch : 현재 진행 프로세스(old) 저장 + 다음 프로세스(new) 부름
scheduler : context switch의 주체

## Process

Job : 수행될 프로그램의 묶음  
Program : 파일  
Process (=running program)  
kernel에 등록되고 관리되는 프로그램(task)  

Process Control Block(PCB)  
프로세스 정보 저장 구조체, 프로세스와 동시 생성  
저장 내용  
프로세스 상태  
프로세스 카운터(다음 실행 주소)  
레지스터, 프로세스 번호(pid), 프로세스 정보  

Process API(Linux) : create, destroy  
fork : 새 process(child) 생성  
exec : child가 새 주소 찾아 나감(집 나감)  
wait : 상위 프로세스가 하위 프로세스 종료를 기다림  

Process Status  
wait : resource free 대기 상태  
new -> ready : OS가 메모리에 탑재  
ready -> running : dispatch  
running -> terminate : exit  
running -> ready : interrupt  
waiting(blocked) : I/O interrupt or event 관련  

좀비 : 자식이 종료 되었는데, 부모가 리소스를 회수를 못함 (해결 : 입양해서 죽이기)  
고아 : 부모가 죽었는데 자식이 실행 중  

스케쥴링 큐  
ready 큐 : 메모리 대기 task의 작업 순서 정리  
I/O 큐 : request 들어왔을대 순서 정리  
디바이스 큐 : 디바이스 제어 대기 프로세스 집합  

## Scheduling

정의 : 시간(Processor), 공간(Memory) 자원을 관리하는 기술  
목표 : 성능 향상  
평가 지표:  
Turnaround Time : ready ~ complete 까지의 시간  
Response(Waiting) Time : ready ~ first run까지의 시간  
Throughput(처리율), fairness, utilization(cpu 수행비율)  

선점(preemptive) scheduling : CPU 사용권을 OS가 선점을 해서 강제 회수 가능.  
비선점(non-preemptive) scheduling : 프로세스의 실행을 강제종료 하지 않는 이상 보장  

burst : 실제 처리시간(일반적으로, CPU burst)  

스케쥴링 계획  

1) FCFS, FIFO (Fist Come~) : 선입 선출(비선점)  
단점 - Convoy effect  

2) SJF(Shortest Job First) : burst time 짧은 순  
단점 - Starvation, 미래 예지가 필요  

3) Round Robin : 주어진 시간(Time Slice = Time Quantum)만큼만 시행(선점)  
Incorporatin I/O  

4) Priority : 우선도라는 지표 순으로 스케쥴링  
단점을 aging 이라는 우선도 가산점으로 극복  
priority 낮은 순서대로  

5) MLFQ(Mulit-Level Feedback Queue)  
과거의 수치로 미래를 예측  
복수의 큐로 여러 스케쥴링 계획 사용 가능  

## Memory

메모리의 추상화 : Virtual Memory  

Fragmentation(파편화)  
Internal(내적) fragmentation  
External(외적) fragmentation  
파편화 최소화를 위해 배치, 할당을 잘해야한다.  

배치 전략  
First-Fit, Best-Fit, Worst-Fit, Next-Fit, Buddy-Algorithm  

연속 메모리 할당  
빈공간 통합, 저장공간 압축  

불연속 메모리할당  
Segmentation : 프로세스를 서로 크기가 다른 논리적인 블록 단위인 '세그먼트(Segment)'로 분할하고 메모리에 배치하는 것  
segement table  

TLB (Translation Look-aside Buffer) : 변환 정보를 여기서 찾으면, 페이지 테이블까지 안가도 빠른 변환이 가능하다.  

## Paging

정의 : 구분없이 모든 data를 동일한 사이즈로 나눠서 관리
page table에 page번호와 offset으로 관리

page 크기가 작아짐  
= page 수가 많아짐  
= page table 커짐  
= fragmentation 작아짐  
= context switch 처리 비용 증가  

## Page Replacement

swap space : 보조기억장치로 확보한 공간
Demand Paging :

페이지 교체 : page fault시 어디에 필요한 페이지를 교체할지 위치 결정하는 방법

- FIFO
- MIN(OPT) 알고리즘 : 이상적 알고리즘, 미래예지 필요.
  - LUR/LRU(Least Recently Used) : 가장 사용된지 오래된걸 교체
- LRU Approximation Algorithm : LRU overhead 비싸서 사용
  - NUR, NRU(Not Recently Used) : 비트 2개로 대체
    -참조비트(use bit, reference bit), 변형비트(dirty bit, update bit)
  - 클락알고리즘, (접근 횟수) 카운팅 알고리즘(LFU, MFU)

Thrashing : 페이지 교체하느라 CPU가 프로세스 처리를 안함.
해결) 적정한 다중 프로그래밍 정도를 유지

워킹 셋 : 일정 시간동안 자주 참조하는 페이지들의 집합

## Concurrency, Thread

Thread : 프로세스 내에서의 작업 단위
장점 : 병행성 증진, 자원 효율성
단점 : Concurrency(동시성)

Race Condition(경쟁 상태)
여러 개의 스레드가 하나의 자원을 두고 서로 경쟁
Critical Section(임계 영역)
여러 개의 스레드가 같이 접근해서는 안되는 공유 영역
Mutual Exclusion(상호 배제, Mutex)
임계 영역에 동시에 접근하지 못하게 막는 방법

## Locks

Mutex 구현 방법
lock : 임계구역 사용 권한 획득
unlock : 임계구역 사용 종료

lock 대기 방법
spin, fetch-and-add, yield

## Condition Variables

wait : sleep 상태로 대기
signal : CPU 몇몇 스레드를 깨운다.
broadcast : 다 깨운다.

## Semaphore

Mutex vs Semaphore
세마포어 : 두 개의 함수로 정수 변수를 제어해서 공유자원에 대한 여러 프로세스와 스레드의 접근을 제어

## Deadlock(교착 상태)

자원을 여러 곳에서 사용하려고 할 때 발생

Deadlock 조건 : 4가지 조건이 만족해야 발생
상호 배제(Mutual Exclusion) : 자원은 한 번에 한 프로세스만이 사용할 수 있다.
점유 대기(Hold and Wait) : 최소한 하나의 자원을 점유하고 있으면서 다른 프로세스에 할당되어 사용하고 있는 자원을 추가로 점유하기 위해 대기하는 프로세스가 있어야 한다.
비선점 (No Preemption) : 다른 프로세스에 할당된 자원은 사용이 끝나서 반납할 때까지 강제로 빼앗을 수 없다.
순환 대기 (Circular Wait) : 프로세스의 집합에서 순환 형태로 자원을 대기하고 있어야 한다.

- Deadlock 해결방법
  1. 예방 : 실행되기 전에 다른 스레드가 모두 자원을 뱉게 하면 된다.
  2. 회피 : 안정상태와 비안정상태로 나누어서 항상 안정상태에 두게 한다.
  3. 감지와 해결
  방치 : 해결 비용 > 문제 발생 비용
  감지 : 자원 할당 그래프
  해결 :
  프로세스 종료 (하나씩 중지 or 전부 중지)
  자원 선점 : 교착 상태 자원을 선점 재분배

## IO Devices & SSD

system bus : CPU, 메모리, 주변 장치간에 이어진 채널
DMA(Direct Memory Access) : 주변 장치가 메모리에 직접 접근하여 읽거나 써서 CPU를 다른곳에 쓸 수 있음
가비지 컬렉션 : 모아서 한번에

## FileSystems

파일 시스템 : 자료를 쉽게 발견하고 유지 관리하는 시스템
리눅스의 파일 시스템은 트리 구조

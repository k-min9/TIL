# 컴퓨터 구조

## ISA(Instruction Set Architecture) : 명령어 집합 구조
  
RISC : 간단한 명령어의 집합
CISC : 복잡한 명령어의 집합

R - format : 계산
I - format : 계산 + 전송
J - format : jump

## Arithmetic

ALU : Arithmetic Logic Unit

IEEE 754 : 부동 소수점
모든 소수는 (–1)^s*M*2^E로 표시된다.
정확도 single : 32비트 / double : 64 비트
normalize : 표기법은 하나

## Processor(Data Path)

MIPS 의 다섯 단계:
fetch(가져오기) -> decode -> execute(연산) -> access -> writeback
나누는 이유 : 파이프라인

ex) 한 클럭당 0.5ns가 소요되는 4단계 파이프라인이 500개의 명령어를 처리하는 데 걸리는 시간을 구하세요.(단위 : ns)  
answer) 1003*0.5ns = 501.5ns  

Encoder, Decoder, Multiplexer(MUX)  
[ex - 8(in) to 3(out)]

hazard  

## Processor(Pipeline)

Interrupt(하드웨어적): 외부 인터럽트 / 내부 인터럽트  
Traps(SW 인터럽트): Exception, System Call  

## Superscalar, VLIW

SuperScalar : 매 사이클마다 다수의 명령어들이 동시에 실행되는 기술
VLIW (Very Long Instuction Word) : 동시에 수행될 수 있는 명령어들을 컴파일러 수준에서 추출, 하나의 명령어로 압축 수행

## Memory Hierarchy(caching)

메모리 계층 구조  
정의 : 메모리를 크고 빠르고 싸게 쓰는 방법  

SRAM : 캐시 메모리  
DRAM : 메인 메모리  

지역성 (locality)이 있어서 성립  
공간 지역성, 시간 지역성  

- write policy  
  - write through : write에 추가 시간 발생
  - write back : 캐시의 블록만 바로 업데이트

Average Memory Access Time (AMAT) = Hit time + Miss rate × Miss penalty

- example
  - Given
    - I-cache miss rate = 2%
    - D-cache miss rate = 4%
    - Miss penalty = 100 cycles
    - Base CPI (ideal cache) = 2
    - Load & stores are 36% of instructions
  - Miss cycles per instruction
    - I-cache: 0.02 × 100 = 2
    - D-cache: 0.36 × 0.04 × 100 = 1.44
  - Actual CPI = 2 + 2 + 1.44 = 5.44
    - Ideal CPU is 5.44/2 =2.72 times faster

cache miss  
hit rate = 1 - miss rate / 높을수록 좋다.  
AMAT(Average Memory Access Time)  
메모리계층구조 이용시, 접근까지 걸리는 평균시간  

## Memory Hierarchy(VirtualMemory, RAID)

가상 메모리 : 메인 메모리를 더 크게 쓰기 위한 두번째 메모리  
페이지 테이블을 사용하여 구현  
페이지 테이블에서 찾을 수 없으면 page fault  

RAID

## Input/Ouput_System

비동기(Asynchronous) : 버스 동작이 끝나면 다음 동작
동기(Synchronous) : 공통된 주기(clock)마다 다음 동작

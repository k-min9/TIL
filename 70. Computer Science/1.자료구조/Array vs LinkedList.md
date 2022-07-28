# Array vs LinkedList

## Array

- 개요 : 연관된 data를 메모리상에서 연속적이며 순차적으로 미리 할당된 크기만큼 저장하는 자료구조
- 특징 : 고정된 저장 공간, 순차적인 데이터 저장
- 장점 : 조회(접근과 할당)를 빠르게 할 수 있음
- 단점 : 삽입/삭제가 느림. 미리 크기를 정해야 함. 메모리 낭비가 발생할 수 있음. 
  - Dynamic Array로 보완
- 기타
  - Array가 size를 넘어갈 경우 : 더 큰 Array를 선언하여 옮기고 기존 Array는 삭제(Doubling, Dynamic Array)
  - 예측하기 힘들다면 애초에 데이터를 할당 받는 방식인 LinkedList를 사용

## Linked List

- 개요 : 데이터+address로 구성된 Node라는 구조체로 이루어짐.
- 특징 : 물리적으로는 비연속이어도 논리적으로는 연속적인 데이터 구조
- 장점 : 삽입/삭제를 빠르게 할 수 있음
- 단점 : 데이터 조회가 느림
- 기타
  - 다른 자료구조를 구현할때 쓰이는 자료구조

## VS

- Array는 compile 단계에서 Stack memory에 Static Memory Allocation 할당
- L.L은 runtime Heap memory에 Dynamic Memory Allocation 할당

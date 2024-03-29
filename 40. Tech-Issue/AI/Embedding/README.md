# Embedding

서류를 input하고, 해당 서류를 읽은것처럼 대화해보자.

## 절차

1. 텍스트 입력
2. 텍스트를 chunk로 변환
3. chunk 단위로 embedding 수행
4. 질문을 embedding함
5. 유사도를 통해 관련 있는 chunk를 식별
6. chunk와 함께 질문을 chatGPT로 보냄
7. 완성. chatGPT는 그 책을 읽은 것 처럼 답변해 줄 것임

## 01_embedding_text

``` pip
  pip install python-dotenv 
  pip install openai==0.28.1
  pip install langchain
  pip install tiktoken  
  pip install faiss-cpu
```

- 개요 : summary.txt라는 파일을 읽고 embedding함
  - 문제점1. 어느정도 규모가 있는 텍스트면 기본이 100만 토큰이다. 임베딩 ada-002 모델 기준으로 약 400원. 질문 하나하나 임베딩 했다가는 파산한다.
  - 문제점2. rate limit이라는 것이 있다. 시간내에 입력할 수 있는 속도 제한이다. ada-002는 1분에 100만 토큰이상의 입력은 거절한다.
- 심화 & 트러블 슈팅
  - 해결1. 책 내용은 기본 변하지 않는다. embedding한 내용을 저장하여, 재활용한다.
  - 해결2. chunk를 업로드 단위로 쪼갠다. 그걸 분할하여 일부씩 업로드하고, 각각의 반환값을 merge하여 저장한다.
    - 해결2-1. 각각 단위로 저장을 하면 이후 뒷부분만 더 학습하여 붙이는 식으로 차후 학습 내역에 관한 임베딩 api 절약도 가능

### 02_symmetric_search_by_embbedding

- 개요 : 질문을 임베딩하여 임베딩된 텍스트들과 유사성을 비교, langchain에 넣어 함께 GPT에 질문하자.
  - 임베딩과 질답을 굳이 같은 공간에서 할 이유도 없고, 산출만 고려하면 임베딩할 리스크를 줄일 수 있기 때문에 파일을 분리하자.
- 심화
  - ChatPromptTemplate를 이용한 System prompt 추가
- 감상
  - 모델: turbo-16k가 1106보다 좀 더 인간이 답변하는 느낌의 답변이 옴
  - chunk가 커서 그런지 embedding 질문은 system prompt가 상대적으로 잘 먹히지 않음

### 기타

- 토큰 계산
  - 애초에 4096토큰(3.5-turbo) 내지 16385 토큰(3.5-turbo-16k,-1106)만 입력이 가능하다
  - 현실적인 이용을 고려할 경우, 3.5-turbo는 질문에 1000토큰당 약 1원, 출력에 약 3원의 금액이 발생함
  - 출력은 얼마 안되니 무시하고, 질문 한번에 5원씩 발생하는 꼴이다. 제대로 활용하자.
  - 영어가 한국어, 일본어 등에 비해 토큰이 압도적으로 작다. 문제는 유료/무료 구분 없이 기본적으로 번역 수준이 좋지 않다는거다.

# Stored Procedure

- 개요 : DB에 저장된 미리 컴파일 된 SQL 쿼리 집합으로 일련의 작업을 수행 후, 그 결과를 반환함

## 초기값 설정

```sql
CREATE OR REPLACE PROCEDURE schemaName.procedureName(
    input1 IN VARCHAR2,  -- IN 입력변수
    input2 IN VARCHAR2,
    output1 OUT VARCHAR2  -- OUT 출력변수
)
IS
    -- 내부변수와 초기값
    name VARCHAR2(10) := 'apple';
    type VARCHAR2(5) := 'fruit';
BEGIN
    -- 작업수행 코드

END procedureName;
/

```

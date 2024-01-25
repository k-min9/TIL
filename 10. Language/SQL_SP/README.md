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

- 함수 추가

```sql
CREATE OR REPLACE PROCEDURE a.x(
    input1 IN VARCHAR2,
    input2 IN VARCHAR2,
    output1 OUT VARCHAR2
)
IS
    name VARCHAR2(10) := 'apple';
    type VARCHAR2(5) := 'fruit';
    
    FUNCTION y(
        input1 IN VARCHAR2,
        input2 IN VARCHAR2
    )
    RETURN VARCHAR2
    IS
        result VARCHAR2(100);
    BEGIN
        -- 여기에 함수 본문을 작성합니다.
        result := 'Processed ' || input1 || ' and ' || input2;

        RETURN result;
    END y;
BEGIN
    -- 작업수행 코드

    -- 함수 호출 예시
    output1 := y(input1, input2);
    
END x;
/
```

## 변수 설정

- 선택하여 변수에 집어 넣기 (SELECT INTO)

``` sql
SELECT column1, column2, ...
INTO variable1, variable2, ...
FROM table_name
WHERE condition;
```

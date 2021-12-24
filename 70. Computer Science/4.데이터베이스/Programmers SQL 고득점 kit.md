# Programmers SQL 고득점 kit

## 0. 테이블 소개

`ANIMAL_INS` : 동물 보호소에 들어온 동물의 정보를 담은 테이블

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

`ANIMAL_OUTS` : 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |



## 1. SELECT

### 1. 모든 레코드 조회하기

동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문

```sql
SELECT * 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
```

### 2. 역순 정렬하기

동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문

```sql
SELECT NAME, DATETIME 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID DESC
```

### 3. 아픈 동물 찾기

동물 보호소에 들어온 동물 중 아픈 동물의 아이디와 이름을 조회하는 SQL 문

```sql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE INTAKE_CONDITION = 'Sick'
```

### 4. 어린 동물 찾기

동물 보호소에 들어온 동물 중 젊은 동물의 아이디와 이름을 조회하는 SQL 문

```sql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE INTAKE_CONDITION <> 'Aged'
```

### 5. 동물의 아이디와 이름

동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문

```sql
SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
ORDER BY ANIMAL_ID
```

### 6. 여러 기준으로 정렬하기

동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문

단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.

```sql
SELECT ANIMAL_ID, NAME,	DATETIME 
FROM ANIMAL_INS 
ORDER BY NAME, DATETIME DESC
```

### 7. 상위 n개 레코드

동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문

```sql
SELECT NAME 
FROM ANIMAL_INS 
ORDER BY DATETIME 
LIMIT 1
```



## 2. SUM, MAX, MIN

### 1. 최댓값 구하기

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문

```sql
SELECT MAX(DATETIME) AS '시간' 
FROM ANIMAL_INS
```

### 2. 최솟값 구하기

동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문

```sql
SELECT MIN(DATETIME) AS '시간' 
FROM ANIMAL_INS
```

### 3. 동물 수 구하기

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문

```sql
SELECT COUNT(*) 
FROM ANIMAL_INS
```

### 4. 중복 제거하기

동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문

이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

```sql
SELECT COUNT(DISTINCT NAME ) 
sFROM ANIMAL_INS;
```



## 3. GROUP BY

### 1. 고양이와 개는 몇 마리 있을까

동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문. 이때 고양이를 개보다 먼저 조회

```sql
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```

### 2. 동명 동물 수 찾기

동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문

이때 결과는 이름이 없는 동물은 집계에서 제외, 결과는 이름 순으로 조회

```sql
SELECT NAME, COUNT(NAME) as COUNT
FROM ANIMAL_INS 
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
```

### 3. 입양 시각 구하기(1)

09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문. 

이때 결과는 시간대 순으로 정렬

```sql
SELECT HOUR(DATETIME) AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 and HOUR(DATETIME) <= 19
GROUP BY HOUR
ORDER BY HOUR
```

### 4. 입양 시각 구하기(2)

0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문

이때 결과는 시간대 순으로 정렬

```sql
SET @hour := -1; -- 변수 선언

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
```



## 4. IS NULL

### 1. 이름이 없는 동물의 아이디

동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문. 

단, ID는 오름차순 정렬

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS 
WHERE NAME IS NULL
```

### 2. 이름이 있는 동물의 아이디

동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문. 

단, ID는 오름차순 정렬

```
SELECT ANIMAL_ID
FROM ANIMAL_INS 
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID
```

### 3. NULL 처리하기

동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문.

이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시

```sql
SELECT ANIMAL_TYPE,	IFNULL(Name, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
```



## 5. JOIN

### 1. 없어진 기록 찾기

입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문

```sql
SELECT *
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
```

### 2. 있었는데요 없었습니다

보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문

이때 결과는 보호 시작일이 빠른 순으로 조회

```sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A 
JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME
ORDER BY A.DATETIME
```

### 3. 오랜 기간 보호한 동물(1)

아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문.

이때 결과는 보호 시작일 순으로 조회

```sql
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3
```

### 4. 보호소에서 중성화한 동물

보호소에 들어올 당시에는 중성화되지 않았지만, 

보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문

```sql
SELECT B.ANIMAL_ID, B.ANIMAL_TYPE, B.NAME
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.SEX_UPON_INTAKE LIKE 'Intact%'
AND A.SEX_UPON_OUTCOME NOT LIKE 'Intact%'
ORDER BY A.ANIMAL_ID
```



## 6. String, Date

### 1. 루시와 엘라 찾기

동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```

### 2. 이름에 el이 들어가는 동물 찾기

동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문. 

이때 결과는 이름 순으로 조회. 단, 이름의 대소문자는 구분하지 않음

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'
AND NAME LIKE '%el%'
ORDER BY NAME
```

### 3. 중성화 여부 파악하기

중성화된 동물은 `SEX_UPON_INTAKE` 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있음

동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문. 

이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시

```sql
SELECT ANIMAL_ID, NAME,
CASE 
    WHEN SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%' 
    THEN 'O'
    ELSE 'X' END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 4. 오랜 기간 보호한 동물(2)

입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문

이때 결과는 보호 기간이 긴 순으로 조회

```sql
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A RIGHT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY B.DATETIME-A.DATETIME DESC
LIMIT 2
```



### 5. DATETIME에서 DATE로  형 변환

ANIMAL_INS 테이블에 등록된 모든 레코드에 대해, 

각 동물의 아이디와 이름, 들어온 날짜를 조회하는 SQL문

이때 결과는 아이디 순으로 조회

```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```


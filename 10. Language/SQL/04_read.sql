-- 04_read.sql

-- 모든 컬럼에 대하여
SELECT * FROM classmates;

-- id, name 만 조회
SELECT id, name FROM classmates;

-- 앞에서 2개만 조회
SELECT id, name FROM classmates LIMIT 2;

-- 앞에 2개 이후 2개 만 조회(2page)
SELECT id, name FROM classmates LIMIT 2 OFFSET 2;

-- 주소 서울만 조회
SELECT id, name, address FROM classmates WHERE address='서울';

-- 나이를 중복없이 조회
SELECT DISTINCT age FROM classmates;

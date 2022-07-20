-- 08_funciton.sql

-- 모든 레코드의 개수
SELECT COUNT(*) FROM users;

-- age 30이상의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;

-- 최고 부자 이름과 액수 조회
SELECT last_name, first_name, MAX(balance) 
FROM users;

-- 30이상의 잔액 평균
SELECT AVG(balance) FROM users WHERE age >= 30;
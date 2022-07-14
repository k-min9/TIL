-- 10_order_by.sql

-- 나이가 가장 어린 10명
SELECT * FROM users 
ORDER BY age ASC LIMIT 10;

-- 나이 => 성 우선슨위 오름차순 상위 10개
SELECT age, last_name FROM users
ORDER BY age ASC, last_name ASC LIMIT 10;

-- 계좌 잔액 상위 10명의 성/이름 10개 => 부자 10인
SELECT last_name, first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;

-- 10대 부자 10명의 이름 + 잔액 + 나이
SELECT * FROM users
WHERE age >= 10 and age < 20
ORDER BY balance DESC
LIMIT 10;

-- Young & Rich
SELECT balance, age FROM users
-- 어리면서 돈많은
-- ORDER BY age ASC, balance DESC 

-- 돈많은데 어린
-- ORDER BY balance DESC, age ASC

LIMIT 10;
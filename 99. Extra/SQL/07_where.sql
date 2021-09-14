-- 07_where.sql

-- 나이가 30 이상
SELECT * FROM users 
WHERE age >= 30;

-- 나이가 30 이상의 이름
SELECT first_name FROM users 
WHERE age >= 30;

-- 나이 30이상, 성 김
SELECT age, last_name FROM users
WHERE age >= 30 AND last_name='김';
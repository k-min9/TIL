-- 09_like.sql

-- 20대 조회
SELECT AVG(age) FROM users 
-- WHERE age >= 20 AND age < 30;
WHERE age LIKE '2_';

-- 지역번호 02
SELECT phone FROM users
WHERE phone LIKE '02-%';

-- 이름이 *준 으로 끝나는 사람
SELECT * FROM users
WHERE first_name LIKE '%준';

-- 중간번호 5114
SELECT phone FROM users
WHERE phone LIKE '%-5114-%';

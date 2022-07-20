-- 11_group_by.sql

-- 같은 성을 가진 사람들의 수
SELECT last_name, COUNT(*) AS name_count 
FROM users
GROUP BY last_name;


-- 성 + 나이가 같은 사람들을 grouping 하여 count
SELECT age, last_name, COUNT(*)
FROM users
GROUP BY age, last_name;

-- 집안 재력 확인 => 성씨
SELECT last_name, AVG(balance) AS asset
FROM users
GROUP BY last_name
ORDER BY asset DESC
LIMIT 10;
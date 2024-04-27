-- 14_oracle_meta.sql
-- 오라클에서 제공하는 meta 정보를 확인할 수 있는 로직을 정리해보자.

-- 테이블 이름과 코멘트를 확인할 수 있다.
SELECT *
FROM ALL_TAB_COMMENTS
WHERE 1=1

-- 테이블의 정보와 소속 컬럼, comment 등을 볼 수 있다.
SELECT *
FROM ALL_COL_COMMENTS
WHERE 1=1

-- 테이블의 정보와 소속 컬럼, data type등을 포함한 컬럼 정보를 볼 수 있다.
SELECT *
FROM ALL_TAB_COLUMNS
WHERE 1=1

-- 테이블의 정보들을 볼 수 있다. 테이블 내용 크기가 보이는 NUM_ROWS가 매우 유용. (갱신시점은 실시간이 아니라 일괄일 가능성이 높음)
SELECT *
FROM ALL_TABLES
WHERE 1=1

-- 인덱스가 적힌 컬럼을 확인할 수 있음. 최적화 등에도 쓰이고,
-- PK 등도 index_name등으로 지정되어 별도 관리될 가능성이 높으므로 pk 파악에도 유용.
SELECT *
FROM ALL_IND_COLUMNS
WHERE 1=1

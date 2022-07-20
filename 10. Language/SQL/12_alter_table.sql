-- 12_alter_table.sql

--  테이블 생성
-- CREATE TABLE articles (
--   title TEXT NOT NULL,
--   content TEXT NOT NULL
-- );


-- 데이터 추가
-- INSERT INTO articles 
-- VALUES ('1번제목', '1번내용');


-- 테이블 이름 변경
ALTER TABLE articles
RENAME TO news;


-- 테이블에 컬럼 추가
ALTER TABLE news 
ADD COLUMN updated_at TEXT NOT NULL DEFAULT 'admin';

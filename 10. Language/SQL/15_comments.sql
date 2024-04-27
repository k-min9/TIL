-- 15_comments.sql
-- DB의 테이블과 컬럼에 메타정보를 넣자.
-- (확인은 테이블정보보기나 메타정보 확인 SQL로 확인)

-- MYSQL 테이블에 comment 추가
ALTER TABLE [테이블명] COMMENT = 'table comment';

-- MYSQL 컬럼에 comment 추가
ALTER TABLE [테이블명] MODIFY [컬럼명] [데이터타입] [제약조건] COMMENT 'column1 comment';

-- MYSQL 테이블에 comment 추가
COMMENT ON TABLE [테이블명] IS [Comment];

-- MYSQL 컬럼에 comment 추가
COMMENT ON COLUMN [테이블명].[컬럼명] IS '[Comment]';

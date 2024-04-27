-- 13_select_for_update.sql
-- DB에서 특정 레코드를 선택하고 해당 레코드를 다른 트랜잭션에서 수정하지 못하도록 잠그는 SQL 구문

START TRANSACTION;

-- 회원 정보 테이블에서 특정 회원 정보를 선택하여 잠금
SELECT * FROM members WHERE member_id = 'some_id' FOR UPDATE;
-- 회원 정보 수정 작업 수행
UPDATE members SET name = 'New Name' WHERE member_id = 'some_id';

-- 해당 회원이 작성한 게시물 정보 테이블에서도 특정 회원의 게시물을 선택하여 잠금
SELECT * FROM posts WHERE author_id = 'some_id' FOR UPDATE;
-- 해당 회원의 게시물 수정 작업 수행
UPDATE posts SET content = 'New Content' WHERE author_id = 'some_id';


COMMIT;

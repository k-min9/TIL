-- 01_create_table.sql

CREATE TABLE classmates (
  id INTEGER PRIMARY KEY, -- AUTOINCREMENT, => 마지막 레코드 삭제되어도 알아서 id ++
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

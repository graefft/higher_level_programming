-- Convert to utf-8
-- Convert database
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert table
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

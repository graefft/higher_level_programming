-- Script that creates table `unique_id` on MySQL server
-- Create table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);

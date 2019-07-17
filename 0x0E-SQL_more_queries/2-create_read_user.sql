-- Script that creates db `hbtn_0d_2` and user `user_0d_2`

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

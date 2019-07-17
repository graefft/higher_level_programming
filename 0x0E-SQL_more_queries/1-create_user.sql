-- Script to create user `user_0d_1`

-- Create user and set password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reset privileges
FLUSH PRIVILEGES;

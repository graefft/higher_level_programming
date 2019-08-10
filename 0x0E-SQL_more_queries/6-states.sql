-- Script that creates database `hbtn_0d_usa` with table `states`

-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

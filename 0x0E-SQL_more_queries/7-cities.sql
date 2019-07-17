-- Script that creates db `hbtn_0d_usa` with table `cities`

-- Create database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL
);
	

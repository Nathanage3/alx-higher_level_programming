-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to hbtn_0d_usa
USE hbtn_0d_usa;

-- CREATE TABLE CITIES
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCE states(id)
);

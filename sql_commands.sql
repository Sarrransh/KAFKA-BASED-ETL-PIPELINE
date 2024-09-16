-- Log in to MySQL as root user
mysql -u root -p

-- Create the database
CREATE DATABASE IF NOT EXISTS weather_db;

-- Use the database
USE weather_db;

-- Create the table
CREATE TABLE IF NOT EXISTS weather_data ( id INT AUTO_INCREMENT PRIMARY KEY, weather_main VARCHAR(255), weather_description VARCHAR(255),main_temp DECIMAL(5,2),main_feels_like DECIMAL(5,2),main_temp_min DECIMAL(5,2),main_temp_max DECIMAL(5,2),main_humidity INT);

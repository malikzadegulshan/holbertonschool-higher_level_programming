-- Create the database hbtn_0d_usa only if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table states only if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,  -- unique, auto-generated, non-null primary key
    name VARCHAR(256) NOT NULL                          -- state name that cannot be null
);
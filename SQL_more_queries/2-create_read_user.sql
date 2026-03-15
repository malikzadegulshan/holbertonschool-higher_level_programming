-- Create the database hbtn_0d_2 only if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user_0d_2 only if it doesn't already exist (prevents failure if user exists)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege to user_0d_2 on all tables in hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Reload privilege tables to ensure changes take effect immediately
FLUSH PRIVILEGES;
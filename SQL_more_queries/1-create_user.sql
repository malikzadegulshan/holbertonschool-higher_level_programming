-- Create user_0d_1 only if it doesn't already exist (prevents failure if user exists)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Reload privilege tables to ensure changes take effect immediately
FLUSH PRIVILEGES;
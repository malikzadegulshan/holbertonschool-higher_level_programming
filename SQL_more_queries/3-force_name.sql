-- Create the table force_name only if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,                     -- integer column (nullable)
    name VARCHAR(256) NOT NULL  -- string column that cannot be null
);
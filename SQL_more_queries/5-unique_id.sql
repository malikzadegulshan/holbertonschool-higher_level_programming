-- Create the table unique_id only if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,  -- integer column with default value 1 and must be unique
    name VARCHAR(256)         -- variable-length string column (nullable)
);
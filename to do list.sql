-- 1. Create the database
CREATE DATABASE tasks_db;

-- 2. Switch to the database
USE tasks_db;

-- 3. Create the tasks table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- unique identifier for each task
    description VARCHAR(255) NOT NULL,   -- the task text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- when the task was added
);

 
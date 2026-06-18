CREATE DATABASE expense_tracker_db;

USE expense_tracker_db;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    amount DECIMAL(10 , 2 ) NOT NULL,
    date DATE NOT NULL,
    payment_method VARCHAR(100) NOT NULL
);

SHOW TABLES;
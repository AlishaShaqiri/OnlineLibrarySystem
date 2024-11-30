CREATE DATABASE IF NOT EXISTS catalog;

USE catalog;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255)
);

INSERT INTO books (title, author) VALUES ('Book A', 'Author A');
INSERT INTO books (title, author) VALUES ('Book B', 'Author B');

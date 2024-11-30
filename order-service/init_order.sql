CREATE DATABASE IF NOT EXISTS `order`;

USE `order`;

CREATE TABLE IF NOT EXISTS `orders` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user_id INT,
    status VARCHAR(255)
);

INSERT INTO `orders` (book_id, user_id, status) VALUES (1, 1, 'Ordered');
INSERT INTO `orders` (book_id, user_id, status) VALUES (2, 2, 'Shipped');

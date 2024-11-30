# Microservices with Independent Databases

## Overview

This project implements a microservices architecture for an **Online Library System**. The system consists of three microservices:

- **Catalog Service**: Manages information about books.
- **User Service**: Manages user profiles.
- **Order Service**: Manages book orders.

Each service has its own MySQL database instance, hosted in separate Docker containers. The services communicate independently and expose APIs for CRUD operations. Docker is used to manage the containers, ensuring the services are isolated and can interact through environment variables.

---

## Prerequisites

Ensure that you have the following tools installed:

- **Docker**: To run the services and databases in containers.

---

## Environment Setup

1. Create a `.env` file in the root of the project and define the environment variables for each microservice’s database credentials:

```env
# Catalog Service DB
DB_HOST=catalog-db
DB_NAME=catalog
DB_USER=catalog_user
DB_PASS=catalog_pass

# User Service DB
DB_HOST=user-db
DB_NAME=users
DB_USER=user_user
DB_PASS=user_pass

# Order Service DB
DB_HOST=order-db
DB_NAME=orders
DB_USER=order_user
DB_PASS=order_pass
Docker Configuration
Dockerfile for Catalog and User Services (Python)
Each Python-based service (catalog-service and user-service) uses Flask and connects to its database through the environment variables. Below is the example Dockerfile:

dockerfile
Copy code
# Dockerfile for Catalog/User Service
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
Dockerfile for Order Service (PHP)
The order-service is written in PHP, using PDO to connect to the MySQL database. Here's the example Dockerfile for the order service:

dockerfile
Copy code
# Dockerfile for Order Service
FROM php:8.0-apache

WORKDIR /var/www/html

COPY . .

EXPOSE 80

CMD ["php", "-S", "0.0.0.0:80"]
How to Run the Project
Clone the repository:
bash
Copy code
git clone <repository-url>
Navigate to the project directory.

Create a .env file and define the environment variables (as shown above).

Build and run the services using Docker:

bash
Copy code
docker build -t catalog-service ./catalog_service
docker build -t user-service ./user_service
docker build -t order-service ./order_service

docker run -d -p 5001:5000 --env-file .env catalog-service
docker run -d -p 5002:5000 --env-file .env user-service
docker run -d -p 5003:80 --env-file .env order-service
Each service will be accessible at:

Catalog Service: http://localhost:5001/catalog
User Service: http://localhost:5002/users
Order Service: http://localhost:5003/orders
API Endpoints
Catalog Service
GET /catalog: Retrieves a list of books.
GET /catalog/{book_id}: Retrieves a specific book by ID.
POST /catalog: Adds a new book to the catalog.
PUT /catalog/{book_id}: Updates a book by ID.
DELETE /catalog/{book_id}: Deletes a book by ID.
Example:

json
Copy code
GET /catalog
[
  {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "year": 2008
  }
]
User Service
GET /users: Retrieves a list of users.
GET /users/{user_id}: Retrieves a specific user by ID.
POST /users: Adds a new user.
PUT /users/{user_id}: Updates a user by ID.
DELETE /users/{user_id}: Deletes a user by ID.
Example:

json
Copy code
GET /users
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
]
Order Service
GET /orders: Retrieves a list of orders.
POST /orders: Adds a new order.
DELETE /orders/{order_id}: Deletes an order by ID.
Example:

json
Copy code
GET /orders
[
  {
    "id": 1,
    "user_id": 1,
    "book_id": 2,
    "status": "shipped"
  }
]
Testing
You can test the endpoints using Postman or curl.

Example Curl Commands:

bash
Copy code
curl http://localhost:5001/catalog
curl http://localhost:5002/users
curl http://localhost:5003/orders
Example Postman Requests:

Send GET requests to the following URLs:
http://localhost:5001/catalog
http://localhost:5002/users
http://localhost:5003/orders
Conclusion
This project demonstrates a microservices-based architecture with separate databases for each service using Docker. The system allows for the creation, retrieval, updating, and deletion of books, users, and orders independently. Each service is connected to its own MySQL database, ensuring clear separation of concerns and maintainability.

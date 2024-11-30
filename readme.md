Microservices with Docker and Independent Databases

Project Overview

This project implements a basic microservices architecture for an Online Library System using Docker. The system comprises three microservices: Catalog Service, User Service, and Order Service, each with its own MySQL database instance. The microservices are managed using Docker Compose and include basic CRUD functionalities, focusing on the READ operation for initial submission.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Microservices and Database Details

1\. Catalog Service

•Language: Python

•Framework: Flask

•Database: MySQL (Catalog Database)

•Functionality: Manages book information (CRUD).

2\. User Service

•Language: Python

•Framework: Flask

•Database: MySQL (User Database)

•Functionality: Manages user profiles (CRUD).

3\. Order Service

•Language: PHP

•Framework: Native PHP

•Database: MySQL (Order Database)

•Functionality: Manages book orders (CRUD).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Environment Setup

Environment Variables

Each service uses the following environment variables to connect to its specific database:

VariableDescriptionExample Value

DB\_HOSTDatabase hostnamecatalog-db, user-db, order-db

DB\_NAMEDatabase namecatalog, users, orders

DB\_USERDatabase usercatalog\_user, user\_user, order\_user

DB\_PASSDatabase passwordcatalog\_pass, user\_pass, order\_pass

Add these variables in a .env file in the root directory of the project.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Docker Configuration

Dockerfile Example

Each microservice has its own Dockerfile. Below is an example for the Python-based services:

dockerfile

Copy code

\# Dockerfile for Catalog/User Service

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD \["python", "app.py"\]

For the Order Service, use the following:

dockerfile

Copy code

\# Dockerfile for Order Service

FROM php:8.0-apache

WORKDIR /var/www/html

COPY . .

EXPOSE 80

CMD \["php", "-S", "0.0.0.0:80"\]

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Docker Compose Configuration

Here’s the docker-compose.yml file to manage the services and databases:

yaml

Copy code

version: '3.8'

services:

catalog:

build:

context: ./catalog\_service

environment:

\- DB\_HOST=catalog-db

\- DB\_NAME=catalog

\- DB\_USER=catalog\_user

\- DB\_PASS=catalog\_pass

networks:

\- library-net

depends\_on:

\- catalog-db

ports:

\- "5001:5000"

catalog-db:

image: mysql:8.0

environment:

MYSQL\_ROOT\_PASSWORD: root

MYSQL\_DATABASE: catalog

MYSQL\_USER: catalog\_user

MYSQL\_PASSWORD: catalog\_pass

networks:

\- library-net

volumes:

\- catalog\_data:/var/lib/mysql

user:

build:

context: ./user\_service

environment:

\- DB\_HOST=user-db

\- DB\_NAME=users

\- DB\_USER=user\_user

\- DB\_PASS=user\_pass

networks:

\- library-net

depends\_on:

\- user-db

ports:

\- "5002:5000"

user-db:

image: mysql:8.0

environment:

MYSQL\_ROOT\_PASSWORD: root

MYSQL\_DATABASE: users

MYSQL\_USER: user\_user

MYSQL\_PASSWORD: user\_pass

networks:

\- library-net

volumes:

\- user\_data:/var/lib/mysql

order:

build:

context: ./order\_service

environment:

\- DB\_HOST=order-db

\- DB\_NAME=orders

\- DB\_USER=order\_user

\- DB\_PASS=order\_pass

networks:

\- library-net

depends\_on:

\- order-db

ports:

\- "5003:80"

order-db:

image: mysql:8.0

environment:

MYSQL\_ROOT\_PASSWORD: root

MYSQL\_DATABASE: orders

MYSQL\_USER: order\_user

MYSQL\_PASSWORD: order\_pass

networks:

\- library-net

volumes:

\- order\_data:/var/lib/mysql

networks:

library-net:

volumes:

catalog\_data:

user\_data:

order\_data:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Testing

1\. Testing with Postman

Catalog Service:

•Endpoint: GET /catalog

•Example Response:

json

Copy code

\[

{

"id": 1,

"title": "Clean Code",

"author": "Robert C. Martin"

},

{

"id": 2,

"title": "The Pragmatic Programmer",

"author": "Andy Hunt"

}

\]

User Service:

•Endpoint: GET /users

•Example Response:

json

Copy code

\[

{

"id": 1,

"name": "Alice",

"email": "alice@example.com"

},

{

"id": 2,

"name": "Bob",

"email": "bob@example.com"

}

\]

Order Service:

•Endpoint: GET /orders

•Example Response:

json

Copy code

\[

{

"id": 1,

"user\_id": 1,

"book\_id": 2

},

{

"id": 2,

"user\_id": 2,

"book\_id": 1

}

\]

2\. Testing with Curl

Run the following commands to test the services:

bash

Copy code

curl http://localhost:5001/catalog

curl http://localhost:5002/users

curl http://localhost:5003/orders

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

How to Run the Project

1.Clone the repository:

bash

Copy code

git clone

2.Navigate to the project directory.

3.Create a .env file with environment variables as shown above.

4.Build and start the services:

bash

Copy code

docker-compose up --build

5.Test the services using Postman or Curl.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Screenshots

Attach screenshots of Postman requests showing responses for /catalog, /users, and /orders endpoints.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Conclusion

This documentation outlines the implementation of a microservices architecture for an Online Library System using Docker. It demonstrates service independence, database isolation, and basic CRUD functionalities, achieving interoperability between microservices.
from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# Get environment variables for DB connection (configured via Docker)
db_host = os.getenv('DB_HOST', 'localhost')
db_name = os.getenv('DB_NAME', 'catalog')
db_user = os.getenv('DB_USER', 'catalog_user')
db_pass = os.getenv('DB_PASS', 'catalog_pass')

# Database connection function
def get_db_connection():
    conn = mysql.connector.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_pass
    )
    return conn

@app.route('/catalog', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({"books": books})

@app.route('/catalog/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id = %s;", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

@app.route('/catalog', methods=['POST'])
def add_book():
    new_book = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (%s, %s, %s);",
        (new_book['title'], new_book['author'], new_book['year'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_book), 201

@app.route('/catalog/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s;",
        (data['title'], data['author'], data['year'], book_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Book updated"}), 200

@app.route('/catalog/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s;", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Book deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)

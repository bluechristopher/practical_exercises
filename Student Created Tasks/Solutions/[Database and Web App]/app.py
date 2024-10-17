from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('LIBRARY.db')
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM Book
            INNER JOIN AuthorBook
            ON Book.book_id = AuthorBook.book_id
            INNER JOIN Author
            ON AuthorBook.author_id = Author.author_id       
    """)

    books = cursor.fetchall()

    conn.close()

    print(books)

    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
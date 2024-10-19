from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# index.html
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Library Catalog</title>
        <meta charset="utf-8">
        <style>
            body {
                font-family: Arial;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Library Catalog</h1>
        <h2>Search</h2>
        <form method="GET">
            <label for="search_title">Title:</label>
            <input type="text" id="search_title" name="search_title">
            <br><br>
            <label for="search_title">Author:</label>
            <input type="text" id="search_author" name="search_author">
            <br><br>
            <input type="submit" value="Search"></label>
        </form>
        <br>
        <h2>Results</h2>
        {% if book_count == 0 %}
            <p> No books found </p>
        {% else %}
            <table>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Author</th>
                    <th>Copies</th>
                </tr>
                {% for book in books %}
                <tr>
                    <td>{{ book[1] }}</td>
                    <td>{{ book[4] }}</td>
                    <td>{{ book[-2] + " " + book[-1] }}</td>
                    <td>{{ book[-6] }}</td>
                </tr>
                {% endfor %}
            </table>
        {% endif %}
    </body>
</html>
"""

@app.route('/')
def home():
    conn = sqlite3.connect('LIBRARY.db')
    cursor = conn.cursor()


    search_title = request.args.get('search_title')
    search_author = request.args.get('search_author')

    try:
        search_title = search_title.title()
    except:
        pass

    try:
        search_author = search_author.title()
    except:
        pass

    if search_title == None and search_author == None:
        cursor.execute("""
                SELECT * FROM Book
                INNER JOIN AuthorBook
                ON Book.book_id = AuthorBook.book_id
                INNER JOIN Author
                ON AuthorBook.author_id = Author.author_id       
        """)
    else:
        if not(search_title != "") and not (search_title != ""):
            search_title = f"%{search_title}%"
            search_author = f"%{search_author}%"
            cursor.execute("""
                SELECT * FROM Book
                INNER JOIN AuthorBook
                ON Book.book_id = AuthorBook.book_id
                INNER JOIN Author
                ON AuthorBook.author_id = Author.author_id
                WHERE Book.title LIKE ? AND Author.first_name LIKE ? OR Author.last_name LIKE ?
            """, (search_title, search_author, search_author))

        elif search_title != "": 
            search_title = f"%{search_title}%"
            cursor.execute("""
                SELECT * FROM Book
                INNER JOIN AuthorBook
                ON Book.book_id = AuthorBook.book_id
                INNER JOIN Author
                ON AuthorBook.author_id = Author.author_id
                WHERE Book.title LIKE ?
            """, (search_title,))
        else:
            search_author = f"%{search_author}%"
            cursor.execute("""
                SELECT * FROM Book
                INNER JOIN AuthorBook
                ON Book.book_id = AuthorBook.book_id
                INNER JOIN Author
                ON AuthorBook.author_id = Author.author_id
                WHERE Author.first_name LIKE ? OR Author.last_name LIKE ?
            """, (search_author, search_author))



    books = cursor.fetchall()
    #print(books)

    book_count = len(books)

    conn.close()

    return render_template('index.html', books=books, book_count=book_count)

if __name__ == '__main__':
    app.run(debug=True)
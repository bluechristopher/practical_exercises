# Task 1
You have been tasked with creating a web application for a local library that allows users to search for books based on title or author. The library maintains a database called `LIBRARY.db`, which contains the following tables:

Author(<u>author_id</u>, first_name, last_name)
Book(<u>book_id</u>, title, isbn13, isbn10, description, copies)
AuthorBook(<u>author_id, book_id</u>)
Foriegn Key: author_id references Author(author_id) and book_id references Book(book_id)

Users of the application will be able to search for books and view key information, such as the title, author, description, and the number of copies available. If a book is not found, the application should display a message stating that the book is unavailable.

The library wants the search results displayed in a clean, easy-to-read table with a simple design, and they have specific styling requirements.

You are to create a web application with the following specifications:

Pages:
1. Home page: This page should have a search form that allows users to search for books by title or author. The search results should be displayed on the same page. The search results in a tabular format. The table should have columns for book title, author, description and the number of copies available.

Styling Requirements:
- Font Family: Arial
- Table Width: 100% of the page
- Table Header Color: #f2f2f2

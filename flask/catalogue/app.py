import os
from flask import Flask, render_template, request, jsonify, json
app = Flask(__name__)

booklist = [
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]

filename = './data/books.json'
msg_error = 'No books found'

# default route index
@app.route('/')
def index():
    return 'hello my app'

# endpoint all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(
        books = booklist
    )

# endpoint id single book
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book_id(book_id):
    for book in booklist :
        if book['id'] == int(book_id):
            return book

# endpoint title single book
@app.route('/api/books/<string:book_title>', methods=['GET'])
def get_book_title(book_title):
    for book in booklist :
        if book['titre'] == str(book_title):
            return book

# route json books
@app.route('/books/json', methods=['GET'])
def get_json_books():
    with open(filename) as books_json:
        data = json.load(books_json)
    return render_template('books.html', data=data)

# route json books by title
@app.route('/books/json/<string:book_title>', methods=['GET'])
def get_json_book_by_title(book_title):
    with open(filename) as books_json:
        data = json.load(books_json)
        result = None
        for book in data :
            if book['title'] == str(book_title):
                result = book
        if result:
            return render_template('book-single.html', data=result)
        else :
            return msg_error

# route json books by id
@app.route('/books/json/<int:book_id>', methods=['GET'])
def get_json_book_by_id(book_id):
    with open(filename) as books_json:
            data = json.load(books_json)
            result = None
            result = []

            for book in data :
                if book['pageCount'] == int(book_id):
                    result = book

            if result:
                return render_template('book-single.html', data=result)
            else :
                return msg_error

if __name__ == '__main__':
    app.run(debug=True)

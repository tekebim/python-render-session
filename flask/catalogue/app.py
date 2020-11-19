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


@app.route('/books/json', methods=['GET'])
def load_books():
    # static/data/test_data.json
    # filename = os.path.join(app.static_folder, 'data', 'books.json')
    filename = './data/books.json'

    with open(filename) as test_file:
        data = json.load(test_file)

    return render_template('books.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

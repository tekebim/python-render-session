from flask import Flask, render_template, request, jsonify
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

@app.route('/')
def index():
    return 'hello my app'

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(
            books = booklist
        )

@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return str(book_id)
    # book = request.args.get('id')
    # book = request.args.get('id', type = int)

if __name__ == '__main__':
    app.run(debug=True)

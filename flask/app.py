from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return 'hello DC'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/ma_route/')
@app.route('/ma_route/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

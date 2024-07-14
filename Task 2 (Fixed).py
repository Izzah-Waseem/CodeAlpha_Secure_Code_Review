
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return f"Search results for: {query}"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Simulate checking username and password from environment variables
    if username == os.environ.get('ADMIN_USER') and password == os.environ.get('ADMIN_PASS'):
        return "Welcome, admin!"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')
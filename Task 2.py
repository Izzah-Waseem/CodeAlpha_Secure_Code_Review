from flask import Flask, request, render_template_string

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
    # Simulate checking username and password
    if username == 'admin' and password == 'password':
        return "Welcome, admin!"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)

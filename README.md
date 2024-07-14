# CodeAlpha_Secure_Code_Review
For this task, let's choose Python as the programming language and review a simple web application written using Flask. We'll identify common security vulnerabilities and provide recommendations for secure coding practices.

**Example Python Code for Review**

Consider the following example of a simple Flask web application in **Task 2 file**.

**Identified Vulnerabilities and Recommendations**

**Bandit:**

The bandit tool has identified two potential security issues in your Flask application. Let's address these issues:

**1. Hardcoded Password**

Bandit flagged a hardcoded password in your login route. Hardcoding passwords is a security risk, as it can be easily exploited if the source code is exposed.
**Original Code:**

          @app.route('/login', methods=['POST'])
          def login():
              username = request.form['username']
              password = request.form['password']
              # Simulate checking username and password
              if username == 'admin' and password == 'password':
                  return "Welcome, admin!"
              else:
                  return "Invalid credentials"

**Solution:**

You should replace hardcoded credentials with a more secure method, such as using environment variables or a secure database lookup. Here's an example using environment variables:
  
    Import os
    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        # Simulate checking username and password from environment variables
        if username == os.environ.get('ADMIN_USER') and password == os.environ.get('ADMIN_PASS'):
            return "Welcome, admin!"
        else:
            return "Invalid credentials"

**Note:** 
Make sure to set the environment variables ADMIN_USER and ADMIN_PASS in your environment.

**2. Debug Mode Enabled**

Running a Flask application with debug=True is dangerous in a production environment because it allows code execution via the Werkzeug debugger.
**Original Code:**

    if __name__ == '__main__':
        app.run(debug=True)

**Solution:**

Only enable debug mode in a development environment. Use an environment variable to control the debug setting:

    if __name__ == '__main__':
        app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')

By following these steps, we can secure your Flask application and address the issues identified by Bandit.

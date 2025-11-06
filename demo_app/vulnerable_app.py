# WARNING: This app contains INTENTIONAL security vulnerabilities
# For educational/testing purposes ONLY - DO NOT deploy to production

from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# setup simple db
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)''')
    
    # add some test data
    c.execute("DELETE FROM users")  # clear existing
    test_users = [
        ('admin', 'super_secret_pass', 'admin@company.local'),
        ('john', 'password123', 'john@company.local'),
        ('alice', 'alice2023', 'alice@company.local')
    ]
    c.executemany('INSERT INTO users (username, password, email) VALUES (?,?,?)', test_users)
    conn.commit()
    conn.close()

# vulnerable login - SQL injection here
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # VULN: SQL injection - directly concatenating user input
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(query)  # executing unsafe query
        user = c.fetchone()
        conn.close()
        
        if user:
            return f"<h1>Welcome {user[1]}!</h1><p>Email: {user[3]}</p><a href='/login'>Logout</a>"
        else:
            return "<h1>Login failed</h1><p>Try: admin/password or use SQL injection</p><a href='/login'>Back</a>"
    
    return '''<!DOCTYPE html>
        <html>
        <head><title>Vulnerable Login</title></head>
        <body>
            <h2>Login Page</h2>
            <form method="post">
                Username: <input name="username" required><br><br>
                Password: <input name="password" type="password" required><br><br>
                <input type="submit" value="Login">
            </form>
            <p><small>Hint: Try SQL injection like ' OR '1'='1</small></p>
        </body>
        </html>
    '''

# show all users (another vuln - info disclosure)
@app.route('/users')
def list_users():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT username, email FROM users')
    users = c.fetchall()
    conn.close()
    
    html = "<h2>Registered Users</h2><ul>"
    for user in users:
        html += f"<li>{user[0]} - {user[1]}</li>"
    html += "</ul><a href='/login'>Login</a>"
    return html

@app.route('/')
def index():
    return '''<h1>Vulnerable Demo App</h1>
              <p>A deliberately insecure web app for penetration testing practice</p>
              <ul>
                  <li><a href="/login">Login Page (SQL Injection)</a></li>
                  <li><a href="/users">View Users (Info Disclosure)</a></li>
              </ul>
              <p><b>Vulnerabilities:</b> SQL Injection, Information Disclosure, No CSRF protection</p>
              '''

if __name__ == '__main__':
    init_db()
    print("[!] Starting vulnerable app on http://localhost:5000")
    print("[!] Try SQL injection: username = ' OR '1'='1 -- ")
    app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)
DATABASE = 'usuarios.db'

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()

initialize_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usuarios', methods=['GET', 'POST'])
def manage_users():
    conn = get_db_connection()
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        conn.execute('INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)',
                     (nombre, password_hash))
        conn.commit()

    cursor = conn.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()

    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=5800)

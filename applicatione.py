
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from database import setup, insert

app = Flask(__name__)
setup.create_tables()

app.secret_key = 'abc'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '979063554'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)


@app.route('/login', methods= ['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            message = 'Logged in successfully!'
            return render_template('home.html', message = message)
        else:
            message = 'Incorrect username / password !'
    return render_template('login.html', message = message)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username',None)
    return redirect(url_for('login'))


@app.route('/register')
def register_render():
    
    return render_template('register.html', message = '')

@app.route('/register', methods=['POST'])
def register():
    message = ''
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    second_password = request.form['second_password']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
    account = cursor.fetchone()
    if account:
        message = 'la cuenta ya existe'
    elif password != second_password:
        message = "las contraseñas no coindicen"
    else:
        cursor.execute('INSERT INTO user (username, email, password, second_password) VALUES (% s, % s, % s, % s)',(username, email, password, second_password))
        mysql.connection.commit()
    return render_template('register.html', message = message)
'''
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':# and 'username' in request.form and 'password' in request.form and 'second_password' in request.form and 'email' in request.form:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        second_password = request.form['second_password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            message = 'La cuenta ya existe !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'email invalido !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            message = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s, % s,)', (username, email, password, second_password, ))
            mysql.connection.commit()
            message = 'You have successfully registered !'
        print("a")    
    elif request.method == 'POST':
        message = 'Please fill out the form !'
        print("b")
    return render_template('register.html', message = message)

'''
@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template("home.html")
    return render_template('home.html')


@app.route('/carrito')
def cart():
    # carrito = True
    return render_template('carrito.html')


# API

@app.route('/users', methods=['GET'])
def get_users():
    data = insert.select_all_users()

    if data:
        return jsonify({'tasks': data})
    elif data == False:
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'tasks': {}})


@app.route('/productos', methods=['GET'])
def get_products():
    data = insert.select_all_products()

    if data:
        return jsonify({'productos': data})
    elif data == False:
        return jsonify({'message': 'Internal Error'})
    else:
        return jsonify({'tasks': {}})

if __name__ == '__main__':
    app.run(host="localhost", port= int("5000"))

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config

# Models:
from modelos.model_user import ModelUser

# Entities:
from modelos.entidades.user import User



app = Flask(__name__)


db = MySQL(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #print(request.form['username'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/store5.html')
        else:
            flash("User not found...")
            return render_template('auth/store5.html')
    else:
        return render_template('auth/sig-in.html')



@app.route('/home')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.config.from_abject(config['development'])
    app.run()

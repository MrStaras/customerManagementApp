from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)

# --- Configuration ---
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- Initialize extensions ---
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# --- Import models AFTER db is defined ---
from models import User, Customer

# --- User loader for Flask-Login ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Routes ---
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('customers'))
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/customers')
@login_required
def customers():
    all_customers = Customer.query.all()
    return {"customers": [c.name for c in all_customers]}

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))

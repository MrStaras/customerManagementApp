from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')



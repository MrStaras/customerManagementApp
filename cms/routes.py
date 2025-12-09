from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, Client

#1. Define the Blueprint
main_bp = Blueprint('main', __name__)

#2. Define root route
@main_bp.route('/')
def index():
    # Redirects to the login page defined in auth.py
    return redirect(url_for('auth.login'))

#3. Define dashboard route
@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

#4. Define clients route
@main_bp.route('/clients')
@login_required
def clients():
    # 1. Handle "Add Client" Form Submission
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        company = request.form.get('company')
        # Default status to 'Active' if not provided
        status = request.form.get('status') or 'Active' 

        new_client = Client(name=name, contact_info=contact, company=company, status=status)
        
        db.session.add(new_client)
        db.session.commit()
        flash('Client added successfully!')
        return redirect(url_for('main.clients'))

    # 2. Fetch Real Data from Database
    all_clients = Client.query.all()
    
    return render_template('clients.html', clients=all_clients)
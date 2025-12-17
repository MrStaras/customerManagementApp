from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import db, Client
from .decorators import admin_required

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
@main_bp.route('/clients', methods=['GET', 'POST'])
@login_required
def clients():
# 1. Handle "Add Client" Form Submission
    if request.method == 'POST':
        
        # Only admins can add clients
        if current_user.role != 'Administrator':
            flash('You do not have permission to add clients.', 'error')
            return redirect(url_for('main.clients'))


        name = request.form.get('name')
        contact = request.form.get('contact')
        company = request.form.get('company')
        status = request.form.get('status') or 'Active' 

        new_client = Client(name=name, contact_info=contact, company=company, status=status)
        
        db.session.add(new_client)
        db.session.commit()
        flash('Client added successfully!')
        return redirect(url_for('main.clients'))


    # 2. Fetch data from Database
    all_clients = Client.query.all()
    return render_template('clients.html', clients=all_clients)

# 5. Route to toggle client status
@main_bp.route('/clients/<int:client_id>/toggle')
@login_required
@admin_required
def toggle_status(client_id):
    client = Client.query.get_or_404(client_id)
    # Toggle logic: If Active -> Inactive, Else -> Active
    if client.status == 'Active':
        client.status = 'Inactive'
    else:
        client.status = 'Active'
        
    db.session.commit()
    return redirect(url_for('main.clients'))


# 6. Route to edit client details
@main_bp.route('/clients/edit/<int:client_id>', methods=['GET', 'POST'])
@login_required
@admin_required  # Using your custom decorator
def edit_client(client_id):
    client = Client.query.get_or_404(client_id)

    if request.method == 'POST':
        client.name = request.form['name']
        client.contact_info = request.form['contact'] # Matches your DB model field name
        client.company = request.form['company']
    
        
        db.session.commit()
        flash('Client updated successfully!')
        
        return redirect(url_for('main.clients'))

    return render_template('edit_client.html', client=client)

# 7. Route to delete client
@main_bp.route('/clients/delete/<int:client_id>', methods=['POST'])
@login_required
@admin_required
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    
    db.session.delete(client)
    db.session.commit()
    
    flash('Client deleted successfully!')
    return redirect(url_for('main.clients'))   # Handle "Add Client" Form Submission

# 8. Route to view analytics
@main_bp.route('/analytics')
@login_required
def analytics():
    # Mock data for the analytics page
    data = {
        'total_revenue': '$120,500',
        'growth': '+15%',
        'client_satisfaction': '4.8/5'
    }
    return render_template('analytics.html', data=data)

# 9. Route to view projects
@main_bp.route('/projects')
@login_required
def projects():
    # Mock data for projects
    mock_projects = [
        {'name': 'Website Redesign', 'client': 'NullByte GMBH', 'status': 'In Progress', 'deadline': '2026-12-25'},
        {'name': 'Mobile App', 'client': 'Sentinel LLC', 'status': 'To Do', 'deadline': '2026-01-10'},
    ]
    return render_template('projects.html', projects=mock_projects)

# 10. Route to view tasks
@main_bp.route('/tasks')
@login_required
def tasks():
    # Mock data for tasks
    mock_tasks = [
        {'title': 'Fix Login Bug', 'project': 'Website Redesign', 'assignee': 'Will Smith', 'status': 'Pending'},
        {'title': 'Database Setup', 'project': 'Mobile App', 'assignee': 'Tim Lee', 'status': 'Done'},
    ]
    return render_template('tasks.html', tasks=mock_tasks)
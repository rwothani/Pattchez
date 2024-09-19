from flask import Blueprint, request, session, redirect, url_for, render_template, flash

# Create a blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# Mock user storage for demonstration purposes
users = {}

# Home route for sign-in/up page
@auth_bp.route('/')
def home():
    # Render the sign_in_up.html page first
    return render_template('signin_up.html')

# Route for login
@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if user exists and password is correct (mock check)
    if username in users and users[username] == password:
        session['user_id'] = 1  # Mock user ID
        return redirect(url_for('auth.dashboard'))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for('auth.home'))

# Route for user registration
@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Store user information in the mock database
    if username not in users:
        users[username] = password
        session['user_id'] = 1  # Mock user ID
        flash("Registration successful!", "success")
        return redirect(url_for('auth.dashboard'))
    else:
        flash("User already exists", "error")
        return redirect(url_for('auth.home'))

# Route for logging out
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.home'))

# Route for the main dashboard (index page)
@auth_bp.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' in session:
        return render_template('index.html')
    else:
        flash("Please log in first", "error")
        return redirect(url_for('auth.home'))

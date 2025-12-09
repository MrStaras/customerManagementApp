from flask import Flask
from flask_login import LoginManager
# Import the db object from models so we can initialize it
from .models import db, User 
from .config import Config

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)

    # Initialize Plugins
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Register Blueprints
    # Note: We import them HERE to avoid circular dependencies
    from .routes import main_bp
    from .auth import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    # Create Database Tables (if they don't exist)
    with app.app_context():
        db.create_all()

    return app
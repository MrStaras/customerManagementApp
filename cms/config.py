import os
from dotenv import load_dotenv

# Explicitly load the .env file so os.environ can find the variables
load_dotenv()

class Config:
    # SECRET KEY
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'dev-key-for-local-use-only'

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get('FLASK_SQLALCHEMY_DATABASE_URI') or 'sqlite:///cms.db'

    # SETTINGS
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
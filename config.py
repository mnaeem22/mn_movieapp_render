import os
import secrets

class Config:
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY', '5d6ec26ebed1cf94e7a2d233303805f3')
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
    
    # Production settings
    DEBUG = os.environ.get('FLASK_ENV') == 'development'

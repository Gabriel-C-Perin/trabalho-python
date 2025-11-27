from flask import Flask
from .database import db
import os

def create_app():
    app = Flask(__name__)

    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, '..', 'saude.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    
    from .routes import bp as api_bp
    from .dashboard import bp as dash_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(dash_bp)

    return app